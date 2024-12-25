from django.shortcuts import render
from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests,json

from checkout.models import CheckoutModel
from checkout.serializers import CheckoutModelSerializer

class CheckoutCreateView(CreateAPIView):
    model = CheckoutModel
    serializer_class = CheckoutModelSerializer
    permission_classes = [AllowAny]


class CheckoutDestroyView(DestroyAPIView):
    model = CheckoutModel
    serializer_class = CheckoutModelSerializer
    permission_classes = [AllowAny]


class KhaltiPaymentInitiateView(APIView):
    def post(self,request,*args,**kwargs):
        khalti_url = "https://a.khalti.com/api/v2/epayment/initiate/"
        headers = {
            'Authorization':'key 7347c42b965b483ba2c97f586b37da19',
            'Content-Type':'application/json',
        }
        try:
            response = requests.post(khalti_url, headers=headers, data=json.dumps(request.data))
            print('response data',response.data)
            print('response status',response.status_code)
            print('response text',response.text)
            return Response(response.json(),status = response.status_code)
        except:
            return Response(
                {"error": "Error connecting to Khalti API"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )



class KhaltiPaymentVerify(APIView):
    pidx = None
    def get(self,request,*args,**kwargs):
        dic = json.loads(request.GET.get('status')) # raw dictionary 
        tt = dic.get('query') # parent key of actual informations/values
        pidx = tt.get('pidx') # pidx 
        self.pidx = pidx

        khalti_verify_url = "https://a.khalti.com/api/v2/epayment/lookup/"
        headers = {
            'Authorization':'key 7347c42b965b483ba2c97f586b37da19',
            'Content-Type':'application/json',
        }
        print('self ',self.pidx)
        response = requests.post(khalti_verify_url,headers=headers,data = json.dumps({'pidx':pidx}))
        resp = json.loads(response.text)
        if resp.get('status') == 'completed':
            print('success')
        return Response({'status':'cool'})
