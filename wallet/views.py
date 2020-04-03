from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from zeep import Client

from .models import PurchaseHistory
from .forms import ZarinpalForm
from zarinpal.settings import ZARINPAL_MERCHANT_ID as MERCHANT

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

def send_request(request):
    form = ZarinpalForm(request.POST or None)
    if form.is_valid():
        amount = form.data['amount']
        if amount != None and len(amount)>0 :
            if int(amount)<2000 :
                return HttpResponse('The minimum charge should be 2000 TOMAN')

            description = "شارژ کیف پول"
            email = form.data['email']
            mobile = form.data['phone']
            domain = request.get_host()
            CallbackURL = domain +'/api/zarinpal/verify/'
            result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
            if result.Status == 100:
                instance = PurchaseHistory(name=form.data['name'] , phone=mobile , email=email , price=amount , Authority=result.Authority)
                instance.save()
                return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
            else:
                return HttpResponse('Error code: ' + str(result.Status))
        else:
            return HttpResponse('Invalid input value')
    context = {'form' : form}
    return render(request , 'send_request.html' , context)


def verify(request):
    if request.GET.get('Status') == 'OK':
        autho = request.GET.get('Authority')
        try:
            obj = PurchaseHistory.objects.get(Authority=autho)
        except:
            return HttpResponse('Invalid Authority Code')
        amount = obj.price
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        obj.Status = result.Status
        obj.RefID = result.RefID
        obj.save()
        if result.Status == 100:
            obj.is_paid = True
            obj.save()
            return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted')
        else:
            return HttpResponse('Transaction failed . error code : ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')



