from django import forms



class ZarinpalForm(forms.Form):
    name = forms.CharField(max_length=255 , label="نام و نام خانوادگی")
    email=forms.EmailField(label='ایمیل')
    phone = forms.CharField(max_length=13 , label="شماره تماس")
    amount = forms.IntegerField()
