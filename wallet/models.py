from django.db import models


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

    def __str__(self):
        return '%s' % (self.name)