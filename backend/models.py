from django.db import models

class Contact(models.Model):
    name=models.CharField()
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
