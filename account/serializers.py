from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSignupSerializers(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = get_user_model()
        fields = ('username','password')
    
    def create(self,validated_data):
        password = validated_data['password']
        try:
            validate_password(password)
            user = get_user_model().objects.create_user(
                username = validated_data['username'],
                password = password
            )
            return user
        except Exception as e:
            raise serializers.ValidationError({'status':str(e)})

