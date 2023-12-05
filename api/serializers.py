from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate_username(self,value):
        if len(value) < 6:
            raise serializers.ValidationError("نام کاربری نمیتواند کمتر از 6 کارکتر باشد")
        return value








