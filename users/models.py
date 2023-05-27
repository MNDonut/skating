from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = []

    username = models.CharField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    city = models.CharField(max_length=128)
    status = models.BooleanField(default=False)


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='sessions')
    date = models.DateField(default=timezone.now)