from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, UserRegisterSerializer, UserPublicSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny 
import os



# Register
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #token, _ = Token.objects.get_or_create(user=user)
            return Response({
            #    "token": token.key,
                "user": UserPublicSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": UserPublicSerializer(user).data
        }, status=status.HTTP_200_OK)

# Me
class MeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({ "user": UserPublicSerializer(user).data }, status=status.HTTP_200_OK)
    
# Logout
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    

class UpdateProfilePictureView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        if 'profile_picture' in request.FILES:
            if user.profile_picture:
                if os.path.isfile(user.profile_picture.path):
                    os.remove(user.profile_picture.path)

            file = request.FILES['profile_picture']
            if not file.content_type.startswith('image/'):
                return Response({'error': 'File must be an image'}, status=400)
            user.profile_picture = file
            user.save()
            try:
                user.save()
                return Response({
                    "user": UserPublicSerializer(user).data,
                    "message": "Profile picture updated successfully"
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "error": f"Error saving image: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)