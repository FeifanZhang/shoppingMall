# Generated by Django 2.1.2 on 2018-11-15 01:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0014_auto_20181114_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0.00, max_length=5),
            preserve_default=False,
        ),
    ]
