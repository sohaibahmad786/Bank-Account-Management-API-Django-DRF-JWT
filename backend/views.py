from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializer import contact_serilizer

class check(APIView):
    def get(self,request):
        return Response({'name':'Sohaib'})
    
# ______________________ Contact API___________________
class contact_list(ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=contact_serilizer
class contact_detail(RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=contact_serilizer

# Create your views here.
