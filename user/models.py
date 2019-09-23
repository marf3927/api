from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    instagramId = models.CharField(max_length=30)
    phoneNumber = models.TextField()
