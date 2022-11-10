# Generated by Django 4.1.2 on 2022-11-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_uid', models.CharField(max_length=255, null=True, unique=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ecommerce_payment',
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_refunded', models.BooleanField(default=False)),
                ('refunded_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ecommerce_refund',
            },
        ),
    ]