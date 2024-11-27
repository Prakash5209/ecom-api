from rest_framework import serializers

from cart.models import CartItem
from store.serializers import ProductModelSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    class Meta:
        model = CartItem
        exclude = ('user',)
        #fields = '__all__'


class CartItemRetrieveSerializer(serializers.ModelSerializer):
    #product = ProductRetrieveSerializer()
    class Meta:
        model = CartItem
        exclude = ('user',)
        #fields = '__all__'