from django.db import models

from django.contrib.auth import get_user_model

user = get_user_model()

class ProfileModel(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE,related_name="profile")
    avatar = models.ImageField(upload_to="avatar",null=True,blank=True)
    middle_name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.user.id}------------{self.user.username}"
