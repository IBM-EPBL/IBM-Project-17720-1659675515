# Generated by Django 4.0.4 on 2022-11-07 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_genscollectionpayment_dresssize_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paymentdetails',
        ),
        migrations.DeleteModel(
            name='smartfashion',
        ),
        migrations.DeleteModel(
            name='Weddingcollection',
        ),
        migrations.DeleteModel(
            name='WeddingPaymentdetails',
        ),
    ]
