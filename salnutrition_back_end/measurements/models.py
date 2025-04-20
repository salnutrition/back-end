from django.db import models
from users.models import User

class MeasurementType(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    measurementType = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.measurementType.name} - {self.value} - {self.date}"