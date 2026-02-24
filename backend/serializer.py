from rest_framework import serializers
from .models import Contact

class contact_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

    def validate_name(self,value):
        if len(value)<5:
            raise serializers.ValidationError("Please Enter at least 5 charactors")
        return value
    def validate_email(self,value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Please Enter Correct Email")
        return value
    def validate_message(self,value):
        if len(value) < 10:
            raise serializers.ValidationError("Message must contain at least 10 charactors")
        return value