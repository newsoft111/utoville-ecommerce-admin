# Generated by Django 4.1.2 on 2022-10-28 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productimage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
    ]
