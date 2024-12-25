from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from account.models import ProfileModel

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

class ProfileSerializer(ModelSerializer):
    avatar = serializers.ImageField(max_length=None,required=False)
    middle_name = serializers.CharField(max_length=255,required=False)

    class Meta:
        model = ProfileModel()
        fields = ('avatar','middle_name')



class UserDetailSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'profile')

    def update(self, instance, validated_data):
        print(instance)
        #profile_data = validated_data.pop('profile', None)
        #if profile_data:
        #    profile = instance.profile
        #    if 'avatar' in profile_data:
        #        profile.avatar = profile_data['avatar']
        #    if 'middle_name' in profile_data:
        #        profile.middle = profile_data['middle_name']
        #    profile.save()

        #return super().update(instance, validated_data)
