# Generated by Django 2.1.2 on 2018-11-14 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0012_auto_20181111_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='discount',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Discount (%)'),
        ),
    ]