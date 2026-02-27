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
from .models import Student
from .serializer import Student_serilizer
from .models import Account
from .serializer import Account_serilizer
# from .serializer import LoginSerializer
from django.conf import settings
from datetime import datetime, timedelta
from .authentication import JWTAuthentication
  
# ______________________ Student Managment API___________________
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
    

# _____________________Register Banking Account __________
class account_list(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=Account_serilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.AllowAny]

class account_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=Account_serilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.AllowAny]

# # __________________ Login Bank account ___________________
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         account = serializer.validated_data['account']

#         payload = {
#             "id": account.id,
#             "username": account.username,
#             "exp": datetime.utcnow() + timedelta(hours=1)
#         }

#         token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

#         return Response({"token": token}, status=status.HTTP_200_OK)
    
# # ____________________ protectd API ____________________
# class ProtectedView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": f"Hello {request.user.username}, you are authenticated!"})