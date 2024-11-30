from django.shortcuts import render
from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny

from cart.models import CheckoutModel
from cart.serializers import CheckoutModelSerializer

class CheckoutCreateView(CreateAPIView):
    model = CheckoutModel
    serializer_class = CheckoutModelSerializer
    permission_classes = [AllowAny]


class CheckoutDestroyView(DestroyAPIView):
    model = CheckoutModel
    serializer_class = CheckoutModelSerializer
    permission_classes = [AllowAny]

