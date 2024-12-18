from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
import base64
import uuid

from utils.timestamp import TimeStampModel

class CategoryModel(TimeStampModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductModel(TimeStampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="productModel_user")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name="productModel_category")

    title = models.CharField(max_length=255)
    description = tinymce_models.HTMLField()
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=100000,default=0,decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #primary_image = models.ImageField(upload_to="products/primary/", null=True, blank=True)
    brand = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    tags = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)  
            self.slug = slugify(f"{self.title}-{self.id}")
            super().save(update_fields=['slug'])
        else:  
            self.slug = slugify(f"{self.title}-{self.id}")
            super().save(*args, **kwargs)

class ProductColorModel(models.Model):
    productmodel = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_color")
    color = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.color}-{str(self.id)}"

class ProductSizeModel(models.Model):
    productmodel = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_size")
    size = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.size}-{str(self.id)}"


class ProductImageModel(models.Model):
    productmodel = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="productmodel_image")
    image = models.ImageField(upload_to="product_image")

    def __str__(self):
        return f"{self.productmodel.title}-{self.image}"



