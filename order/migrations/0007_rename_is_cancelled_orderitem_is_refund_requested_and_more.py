# Generated by Django 4.1.2 on 2022-11-08 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0001_initial'),
        ('order', '0006_orderitem_delivered_at_orderitem_is_delivered_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='is_cancelled',
            new_name='is_refund_requested',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='cancelled_at',
            new_name='refund_requested_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pg_uid',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='is_refunded',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='refunded_at',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.payment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='used_point',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='refund',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charge.refund'),
        ),
    ]
