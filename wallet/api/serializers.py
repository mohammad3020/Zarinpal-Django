from rest_framework.serializers import ModelSerializer
from wallet.models import *


class SendRequestSerializer(ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = [
           'name',
            'email',
            'phone',
           'price',

        ]




class VerifySerializer(ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = [
           'price',
            'user'
        ]