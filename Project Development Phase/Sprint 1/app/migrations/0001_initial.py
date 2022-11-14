# Generated by Django 4.1.3 on 2022-11-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Getintough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='smartfashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress_name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('1', 'Green'), ('2', 'Red'), ('3', 'Blue'), ('4', 'LiteBlue')], default='1', max_length=20)),
                ('size', models.CharField(choices=[('1', 'M'), ('2', 'S'), ('3', 'L'), ('4', 'XL'), ('4', 'XXL')], default='1', max_length=20)),
                ('dressprice', models.CharField(max_length=100)),
                ('dressqnty', models.CharField(max_length=100)),
                ('rating1', models.CharField(max_length=100)),
                ('rating2', models.CharField(max_length=100)),
                ('rating3', models.CharField(max_length=100)),
                ('rating4', models.CharField(max_length=100)),
                ('rating5', models.CharField(max_length=100)),
                ('total_amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weddingcollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress_name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('1', 'Green'), ('2', 'Red'), ('3', 'Blue'), ('4', 'LiteBlue')], default='1', max_length=20)),
                ('size', models.CharField(choices=[('1', 'M'), ('2', 'S'), ('3', 'L'), ('4', 'XL'), ('4', 'XXL')], default='1', max_length=20)),
                ('payment', models.CharField(choices=[('1', 'Googlepay'), ('2', 'Paytm'), ('3', 'phonepay'), ('4', 'yespay'), ('5', 'yonosbi')], default='1', max_length=20)),
                ('payment_card', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]