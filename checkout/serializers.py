from rest_framework import serializers

from checkout.models import CheckoutModel

class CheckoutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutModel
        exclude = ('user',)
