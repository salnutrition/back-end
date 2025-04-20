from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', 
        blank=True, 
        null=True, 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username