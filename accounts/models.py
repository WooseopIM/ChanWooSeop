from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
