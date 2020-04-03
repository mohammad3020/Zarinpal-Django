from django.conf.urls import url
from .views import *

app_name = 'wallet'
urlpatterns = [
    url(r'^request/$', SendRequestAPIView.as_view(), name='request'),
    url(r'^verify/$', VerifyAPIView.as_view(), name='verify'),
]
