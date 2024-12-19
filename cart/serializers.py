from rest_framework import serializers

from cart.models import CartItem
from store.serializers import ProductModelSerializer,ProductImageModelSerializer
from store.models import ProductImageModel

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ('user','total_cost',)
        #fields = '__all__'

# serializer for cart list with necessary details only
class CartListSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(read_only=True)
    productmodel_image = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        #exclude = ('user',)
        fields = '__all__'

    def get_productmodel_image(self,obj):
        product_id = obj.product.id
        product_image = ProductImageModel.objects.get(productmodel__id = product_id)
        product_image_serializer = ProductImageModelSerializer(product_image)
        return product_image_serializer.data
