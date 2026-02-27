from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Account(AbstractUser):
    full_name=models.CharField()
    age=models.IntegerField()

    def __str__(self):
        return self.username

# Create your models here.
