# Generated by Django 4.2.1 on 2023-05-23 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_order_status_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
