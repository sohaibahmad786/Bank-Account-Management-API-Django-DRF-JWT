from rest_framework import serializers
from .models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Account_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'
        extra_kwargs={
         'username':{
             'required':True,'allow_blank':False,
             'error_messages':{
                 'required':"please Enter username",
                 'allow_blank':"please Enter Password"
             }
         },
         'password':{
             'required':True, 'allow_blank':False,
             'error_messages':{
                 'required':"please Enter Password",
                 'allow_blank':"please Enter Password",
             }
         }
        }

    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError("Please Enter Strong Password minimium 8 chars")
        return value
    
    def validate_age(self,value):
        if value < 18:
            raise serializers.ValidationError("Sorry your age is not now to make account")
        return value
    
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    def update(self,instance,validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().update(instance,validated_data)
        
