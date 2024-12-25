from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from account.serializers import UserSignupSerializers,UserDetailSerializer
from account.models import ProfileModel

user = get_user_model()

# helper function to know the user from api key || token
def know_user(token):
    user_id = AccessToken(token.split(' ')[1])['user_id']
    return user_id

# create profile after post_save in user model
@receiver(post_save,sender = user)
def create_profile(sender,instance,created,**kwargs):
    ProfileModel.objects.create(user = instance)
    
class ProfileInfo(APIView):
    def get(self,request):
        val = know_user(request.headers.get('Authorization'))
        user_detail = user.objects.get(id = val)
        seri = UserDetailSerializer(user_detail)
        return Response(seri.data,status = status.HTTP_200_OK)

class UserSignup(APIView):
    def post(self,request,*args,**kwargs):
        seri = UserSignupSerializers(data = request.data)
        if seri.is_valid():
            user = seri.save()
            return Response(seri.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
