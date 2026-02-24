from django.db import models

class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
