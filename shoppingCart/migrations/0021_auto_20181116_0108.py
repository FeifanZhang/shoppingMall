# Generated by Django 2.1.2 on 2018-11-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0020_auto_20181116_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='addressee',
            field=models.CharField(max_length=128),
        ),
    ]
