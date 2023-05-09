from django.contrib.auth.models import AbstractUser
from django.db import models
from avatar.models import AvatarField

class CustomUser(AbstractUser):
    name=models.CharField(null=True, blank=True, max_length=100)
    avatarImage = AvatarField(upload_to="avatars/", null=True, blank=True)