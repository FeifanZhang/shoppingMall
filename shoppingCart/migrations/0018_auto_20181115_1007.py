# Generated by Django 2.1.2 on 2018-11-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0017_auto_20181115_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='totalPrice',
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=2),
        ),
    ]