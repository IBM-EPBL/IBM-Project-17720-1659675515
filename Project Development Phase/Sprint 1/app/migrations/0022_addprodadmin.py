# Generated by Django 4.1.1 on 2022-11-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_girlscollectionpayment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addprodadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dressimages', models.ImageField(upload_to='')),
                ('dress_name', models.CharField(max_length=20)),
                ('dress_amount', models.CharField(max_length=10)),
            ],
        ),
    ]