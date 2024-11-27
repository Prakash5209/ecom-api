from rest_framework import status,response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.views import View
from django.http import JsonResponse
from django.db.models import Prefetch

#from store.serializers import ProductSerializer,ProductRetrieveSerializer
#from store.models import Product,ProductImages
from cart.models import CartItem
from cart.serializers import CartItemSerializer,CartItemRetrieveSerializer
#from store import serializers

#exist_or_not = CartItem.objects.filter(user = self.request.user,product = serializer.validated_data['product'],quantity = serializer.validated_data['quantity'],color = serializer.validated_data['color'],size = serializer.validated_data['size']).exists()

class CartListView(ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user)

class CartItemCreateView(CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    #def get_queryset(self):
    #    return CartItem.objects.filter(user = self.request.user) 

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        try:
            exist_or_not = CartItem.objects.get(user = self.request.user,product = serializer.validated_data['product'],color = serializer.validated_data['color'],size = serializer.validated_data['size'])
            exist_or_not.quantity += serializer.validated_data['quantity']
            exist_or_not.save()
            return response.Response(serializer.data,status = status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            self.perform_create(serializer)
            return response.Response(serializer.data,status = status.HTTP_201_CREATED)


    #def create(self, request, *args, **kwargs):
    #    serializer = self.get_serializer(data=request.data)
    #    print('on',serializer)
    #    serializer.is_valid(raise_exception=True)
    #    self.perform_create(serializer)
    #    headers = self.get_success_headers(serializer.data)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

#class CartItemRUD(APIView):
#    def get(self,request,pk):
#        modl = CartItem.objects.get(id = pk,user = request.user)
#        seri = CartItemSerializer(self.modl)
#        return response.Response(seri.data,status=status.HTTP_200_OK)
#
#    def patch(self,request,pk):
#        modl = CartItem.objects.get(id = pk,user = request.user)
#        seri = CartItemSerializer(modl,partial=True,data= request.data)
#        if seri.is_valid():
#            seri.save()
#            print(seri.data)
#            return response.Response(seri.data,status=status.HTTP_200_OK)
#        return response.Response(seri.data,status=status.HTTP_404_NOT_FOUND)
#
#    def delete(self,request,pk):
#        modl = CartItem.objects.get(id = pk,user = request.user)
#        return modl.delete()


class CartItemRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, user=request.user)
        except CartItem.DoesNotExist:
            return Response({"status": "cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print('data saved',serializer.data)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
