from django.urls import path

from cart.views import CartItemCreateView,CartItemRUD,CartListView

app_name = "cart"
urlpatterns = [
    path('api/',CartItemCreateView.as_view(),name="cart"),
    path('api/list/',CartListView.as_view(),name="cartlist"),
    path('api/cart-operation/<int:pk>/',CartItemRUD.as_view(),name="cartoperation") 
]
