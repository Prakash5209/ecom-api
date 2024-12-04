from django.urls import path

from checkout.views import KhaltiPaymentInitiateView

app_name="checkout"
urlpatterns = [
    path('api/khalti-initiate/',KhaltiPaymentInitiateView.as_view(),name="khalti-initiate")
]
