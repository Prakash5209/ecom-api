from django.db import models
from django.contrib.auth.models import User

#from store.models import Category,Product

class TimeStampModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']


class CartItem(TimeStampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart_user')
    #product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=255,blank=True,null=True)
    size = models.CharField(max_length=255,blank=True,null=True)

    #class Meta:
    #    unique_together = ('product','user',)

    def __str__(self):
        return f"{self.product} * {self.quantity} in cart"


    def total_price(self):
        return self.product.price * self.quantity


    def save(self,*args,**kwargs):
        if self.quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        super().save(*args,**kwargs)
