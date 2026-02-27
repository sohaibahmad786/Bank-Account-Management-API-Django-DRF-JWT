from django.contrib import admin

from .models import Student
from .models import Account

admin.site.register(Account)
admin.site.register(Student)
# Register your models here.
