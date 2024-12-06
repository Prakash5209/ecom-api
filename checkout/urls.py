from django.urls import path

from checkout.views import KhaltiPaymentInitiateView,KhaltiPaymentVerify

app_name="checkout"
urlpatterns = [
    path('api/khalti-initiate/',KhaltiPaymentInitiateView.as_view(),name="khalti-initiate"),
    path('api/khalti-verify/',KhaltiPaymentVerify.as_view(),name="khalti-verify")
]
