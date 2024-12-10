from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from account.serializers import UserSignupSerializers

User = get_user_model()

class UserSignup(APIView):
    def post(self,request,*args,**kwargs):
        seri = UserSignupSerializers(data = request.data)
        if seri.is_valid():
            user = seri.save()
            return Response(seri.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
