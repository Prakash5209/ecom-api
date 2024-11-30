from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from store.models import CategoryModel,ProductModel

class TimeStampModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']


class CartItem(TimeStampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart_user')
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=255,blank=True,null=True)
    size = models.CharField(max_length=255,blank=True,null=True)
    total_cost = models.DecimalField(decimal_places=2,blank=True,null=True,max_digits=600000000)

    #class Meta:
    #    unique_together = ('product','user',)

    def __str__(self):
        return f"{self.product} * {self.quantity} in cart"

    def save(self,*args,**kwargs):
        self.total_cost = self.quantity * self.product.price
        if self.quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        if self.quantity > self.product.stock:
            raise ValueError("quantity got greater than stock cannot save.")
        super().save(*args,**kwargs)
