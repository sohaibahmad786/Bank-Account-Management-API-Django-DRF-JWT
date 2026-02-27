from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    full_name=models.CharField()
    age=models.IntegerField()

    def __str__(self):
        return self.username

# Create your models here.
