# Zarinpal - Django - Django REST
### جنگو - زرین پال

<div dir="rtl">
   پروژه پیش رو یک پروژه نمونه پرداخت زرین پال در Django می باشد که هم بصورت عادی و هم rest نوشته شده است

</div>

#### Requirement
- Python 3.6 & up

#### Install Dependencies
- Django==3.0.5
- zeep==3.4.0
- djangorestframework==3.11.0
- markdown==3.2.1
- django-filter==2.2.0

You can use requirements.txt to install all the above packages
```
pip install -r requirements.txt
```
### Set ZARINPAL MERCHANT ID
Go to the following directory and set ZARINPAL_MERCHANT_ID to your Zarinpal MERCHANT
```
zarinpal/settings.py
```
### Run Project
Suppose the project is run on localhost
```
python manage.py runserver 8000
```
### Model guidance
We have a wallet app and the in modls.py we have PurchaseHistory
```
class PurchaseHistory(models.Model):
    name = models.CharField(max_length=255 , verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=13 , verbose_name="شماره تماس")
    email = models.EmailField(verbose_name="پست الکترنیکی")
    price = models.IntegerField(verbose_name="مبلغ")
    Authority = models.CharField(max_length=50, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    Status=models.CharField(max_length=50 , null=True , blank=True)
    RefID = models.CharField(max_length=50 , null=True , blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
```