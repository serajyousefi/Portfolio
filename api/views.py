from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import *

class UserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        ser_data = serializers.UserSerializer(data = request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username = ser_data.validated_data['username'],
                password = ser_data.validated_data['password'],
            )
            return Response(data = ser_data.data)
        return  Response(data = ser_data.errors)


class UserRead(APIView):
    def get(self, request):
        user = User.objects.all()
        ser_data = serializers.UserSerializer(instance=user, many=True)
        return Response(data = ser_data.data)



class SearchUserById(APIView):
    def get(self,request,id):
        user = User.objects.get(id=id)
        ser_data = serializers.UserSerializer(instance=user)
        return Response(data = ser_data.data)


