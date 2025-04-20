from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Measurement, MeasurementType
from .serializers import MeasurementTypeSerializer


# Get Measurement types
class MeasurementType(APIView):
    def get(self, request):
        MeasurementTypes = MeasurementType.objects.all()
        serializer = MeasurementTypeSerializer(MeasurementTypes, many=True)

        
