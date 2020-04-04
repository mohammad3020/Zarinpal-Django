# Zarinpal - Django - Django REST
### جنگو - زرین پال
![Header](https://i.imgur.com/ksDxzUn.jpg)
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
Go to the following directory and set ZARINPAL_MERCHANT_ID variable to your Zarinpal MERCHANT
```
zarinpal/settings.py
```
### Run Project
Suppose the project is run on localhost
```
python manage.py runserver 8000
```
The project is now running on http://127.0.0.1:8000/ \
You can access the payment page with the following address
```
http://127.0.0.1:8000/web/zarinpal/request/
```
In the opened page, the user must enter his information \
All information is stored in the PurchaseHistory model \
After paying, the user will be redirected to the address below
```
http://127.0.0.1:8000/web/zarinpal/verify/
```
### Django REST
The api has also been implemented \
All code is available in the /wallet/api folder \
The following two addresses have been used to request and verify
```
http://127.0.0.1:8000/api/zarinpal/request/
http://127.0.0.1:8000/api/zarinpal/verify/
```
