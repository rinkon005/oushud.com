# Generated by Django 3.0.4 on 2020-05-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200506_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='Product_name',
        ),
    ]
