# Generated by Django 4.0.4 on 2022-11-10 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_lycrapant_dresscolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesti',
            name='dresscolor',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
