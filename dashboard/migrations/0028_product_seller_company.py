# Generated by Django 4.2.1 on 2023-06-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_alter_inventory_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller_company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]