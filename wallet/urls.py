from django.conf.urls import url
from .views import *

app_name = 'wallet'
urlpatterns = [
    url(r'^request/$', send_request , name='request'),
    url(r'^verify/$', verify, name='verify'),
]
