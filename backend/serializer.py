from rest_framework import serializers
from .models import Student

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
