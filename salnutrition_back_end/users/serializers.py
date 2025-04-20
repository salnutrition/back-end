from .models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User   
        fields = [
            'username', 
            'email',
            'password',
            'first_name',
            'last_name'
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )
        return user
    
class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name","bio", "profile_picture"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)