from rest_framework import serializers
from .models import Student
from .models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class Student_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    extra_kwargs={
        'created_at':{'read_only':True}
    }
    extra_kwargs={
       'email':{
           'required':True,
           'allow_blank':False,
           'error_messages':{
               'required':"please enter email",
               'allow_blank':"Email are compulsory"
           }
       }
       
    }
    def validate_age(self,value):
        if value < 5:
            raise serializers.ValidationError("You are now Child")
        return value
    def validate_course(self,value):
        if not value:
            raise serializers.ValidationError("Please Choose Course")
        return value


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
    
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         username = data.get("username")
#         password = data.get("password")

#         try:
#             account = Account.objects.get(username=username)
#         except Account.DoesNotExist:
#             raise serializers.ValidationError("Invalid username or password")

#         if not check_password(password, account.password):
#             raise serializers.ValidationError("Invalid username or password")

#         data['account'] = account
#         return data