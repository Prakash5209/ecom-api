from django.db import models
from django.contrib.auth.models import User

from cart.models import CartItem

class CheckoutModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='checkout_user')
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    cart = models.ForeignKey(CartItem,on_delete = models.CASCADE,related_name="cartitem")

    def __str__(self):
        return f"{self.cart}"
