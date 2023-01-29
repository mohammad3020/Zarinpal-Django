from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import redirect
from zeep import Client

from wallet.models import PurchaseHistory
from zarinpal.settings import ZARINPAL_MERCHANT_ID as MERCHANT


client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

class SendRequestAPIView(APIView):
    serializer_class = SendRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('price') != None and len(data.get('price'))>0 :
            amount = data.get('price')
            if int(amount)<2000 :
                return Response({'details': 'The minimum charge should be 2000 TOMAN'})
            description = "شارژ کیف پول"
            email=data.get('email')
            mobile = data.get('phone')
            domain = request.get_host()
            CallbackURL = 'http://' + domain +'/api/zarinpal/verify/'
            result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
            if result.Status == 100:
                instance = PurchaseHistory(name=data.get('name') , phone=mobile , email=email , price=amount , Authority=result.Authority)
                instance.save()
                return Response({'redirect to : ': 'https://www.zarinpal.com/pg/StartPay/' + str(result.Authority)},
                                status=200)
            else:
                return Response({'Error code: ' : str(result.Status)},status=400)
        else:
            return Response({'details': 'Invalid input value'})




class VerifyAPIView(APIView):
    serializer_class = VerifySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.GET.get('Status') == 'OK':
            autho = request.GET.get('Authority')
            try:
                obj = PurchaseHistory.objects.get(Authority=autho)
            except:
                return Response({'details': 'Authority Code not found'})
            amount = obj.price
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            obj.Status = result.Status
            obj.RefID = result.RefID
            obj.save()
            if result.Status == 100:
                obj.is_paid = True
                obj.save()
                return Response({'details': 'Transaction success. RefID: ' + str(result.RefID)}, status=200)
            elif result.Status == 101:
                return Response({'details': 'Transaction submitted'}, status=200)
            else:
                return Response({'details': 'Transaction failed . error code : ' + str(result.Status) }, status=200)
        else:
            return Response({'details': 'Transaction failed or canceled by user'}, status=200)

