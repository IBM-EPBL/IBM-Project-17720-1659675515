# Generated by Django 4.1.3 on 2022-11-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_feedback_weddingcollection_dressprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dressname', models.CharField(max_length=100)),
                ('dressqnty', models.CharField(max_length=100)),
                ('dressamount', models.CharField(max_length=100)),
                ('Customername', models.CharField(max_length=100)),
                ('paymentstype', models.CharField(choices=[('Paytm', 'Paytm'), ('GooglePay', 'GooglePay'), ('Freecharge', 'Freecharge'), ('YonoSBI', 'YonoSBI'), ('Payzapp', 'Payzapp')], default='1', max_length=20)),
                ('accountnumber', models.CharField(max_length=100)),
                ('deliverydate', models.CharField(max_length=100)),
            ],
        ),
    ]
