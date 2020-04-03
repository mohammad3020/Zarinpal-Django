# Generated by Django 3.0.4 on 2020-04-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(max_length=13, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, verbose_name='پست الکترنیکی')),
                ('price', models.IntegerField(verbose_name='مبلغ')),
                ('Authority', models.CharField(blank=True, max_length=50, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('Status', models.CharField(blank=True, max_length=50, null=True)),
                ('RefID', models.CharField(blank=True, max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
