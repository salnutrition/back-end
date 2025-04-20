from rest_framework import serializers
from .models import Measurement, Measurement_type

class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement_type
        fields = ["name","unit"]