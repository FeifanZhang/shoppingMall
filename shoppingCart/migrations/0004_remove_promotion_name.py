# Generated by Django 2.1.2 on 2018-11-10 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0003_auto_20181111_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='name',
        ),
    ]
