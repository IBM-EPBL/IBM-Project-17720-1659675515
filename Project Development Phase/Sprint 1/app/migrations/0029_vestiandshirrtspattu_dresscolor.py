# Generated by Django 4.0.4 on 2022-11-10 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_shirt_dresscolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vestiandshirrtspattu',
            name='dresscolor',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]