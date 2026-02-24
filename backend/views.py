from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions,generics
from .models import Student
from .serializer import Student_serilizer


    
# ______________________ Student Managment API___________________
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
    


# Create your views here.
