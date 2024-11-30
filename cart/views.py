from rest_framework import status,response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.views import View
from django.http import JsonResponse
from django.db.models import Prefetch,Q

#from store.serializers import ProductSerializer,ProductRetrieveSerializer
from store.models import ProductModel
from cart.models import CartItem
from cart.serializers import CartItemSerializer,CartItemRetrieveSerializer,CartListSerializer
#from store import serializers

#exist_or_not = CartItem.objects.filter(user = self.request.user,product = serializer.validated_data['product'],quantity = serializer.validated_data['quantity'],color = serializer.validated_data['color'],size = serializer.validated_data['size']).exists()

class CartListView(ListAPIView):
    serializer_class = CartListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user)

class CartItemCreateView(CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user) 

    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        # necessary item
        pid = serializer.validated_data.get('product').id
        pstock = serializer.validated_data.get('product').stock
        cart_quantity = sum([i.quantity for i in CartItem.objects.filter(Q(product__id = pid) & Q(user = self.request.user))])
        print(request.data)

        try:
            exist_or_not = CartItem.objects.get(user = self.request.user,product = serializer.validated_data['product'],color = serializer.validated_data['color'],size = serializer.validated_data['size'])
            if cart_quantity < pstock:
                exist_or_not.quantity += serializer.validated_data['quantity']
                exist_or_not.save()
                return response.Response(serializer.data,status = status.HTTP_200_OK)
            else:
                return response.Response({'status':'cart quantity is greater than pstock'},status = status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            if cart_quantity+request.data.get('quantity')<= pstock:
                self.perform_create(serializer)
                return response.Response(serializer.data,status = status.HTTP_201_CREATED)
            else:
                return response.Response({'status':'cart quantity is full'},status = status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


    #def create(self,request,*args,**kwargs):
    #    serializer = self.get_serializer(data = request.data)
    #    serializer.is_valid(raise_exception = True)

    #    pid = serializer.validated_data.get('product').id
    #    pstock = serializer.validated_data.get('product').stock
    #    cart_quantity = sum([i.quantity for i in CartItem.objects.filter(product__id = pid)])
    #    print('cart_quantity',cart_quantity)
    #    if cart_quantity >= pstock:
    #        print(cart_quantity)
    #        print(pstock)
    #        raise ValueError("CartItemCreateView: quantity is greater than stock cannot save")
    #    else:
    #        try:
    #            exist_or_not = CartItem.objects.get(user = self.request.user,product = serializer.validated_data['product'],color = serializer.validated_data['color'],size = serializer.validated_data['size'])
    #            exist_or_not.quantity += serializer.validated_data['quantity']
    #            exist_or_not.save()
    #            return response.Response(serializer.data,status = status.HTTP_200_OK)
    #        except CartItem.DoesNotExist:
    #            self.perform_create(serializer)
    #            return response.Response(serializer.data,status = status.HTTP_201_CREATED)

    def perform_create(self, serializer):
            serializer.save(user = self.request.user)


class CartItemRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CartListSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, user=request.user)
        except CartItem.DoesNotExist:
            return Response({"status": "cart item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                total_quantity = sum([i.quantity for i in CartItem.objects.filter(product__id = cart_item.product.id)])
                if total_quantity >= cart_item.product.stock and request.data.get('operation_status') == 'addition':
                    print('no more addition quantity if already full')
                    return response.Response(serializer.data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                else:
                    print('subtraction allowed and saved')
                    serializer.save()
                    return response.Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return response.Response("CartItemRUD: failed to perform the operation",status = status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
