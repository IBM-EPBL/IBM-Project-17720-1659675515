# Generated by Django 4.0.4 on 2022-11-10 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_jean_vestiandshirrtspattu'),
    ]

    operations = [
        migrations.AddField(
            model_name='addprodadmin',
            name='dresscolor',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]