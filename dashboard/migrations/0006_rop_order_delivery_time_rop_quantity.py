# Generated by Django 4.2.1 on 2023-05-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_product_order_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='rop',
            name='order_delivery_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='rop',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
