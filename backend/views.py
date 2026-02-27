from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions,generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Account
from .serializer import Account_serilizer
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication


# _____________________ Banking Account API __________
class account_list(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=Account_serilizer
    permission_classes=[permissions.AllowAny]

class account_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=Account_serilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.AllowAny]
