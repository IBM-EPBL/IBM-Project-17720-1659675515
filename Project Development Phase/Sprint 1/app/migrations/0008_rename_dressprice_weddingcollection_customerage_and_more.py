# Generated by Django 4.1.3 on 2022-11-04 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_paymentdetails_dressprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weddingcollection',
            old_name='dressprice',
            new_name='customerage',
        ),
        migrations.RemoveField(
            model_name='weddingcollection',
            name='dressqnty',
        ),
        migrations.RemoveField(
            model_name='weddingcollection',
            name='rating1',
        ),
        migrations.RemoveField(
            model_name='weddingcollection',
            name='total_amount',
        ),
    ]
