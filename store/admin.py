from django.contrib import admin

from store.models import CategoryModel,ProductModel,ProductColorModel,ProductImageModel,ProductSizeModel

admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProductColorModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductSizeModel)
