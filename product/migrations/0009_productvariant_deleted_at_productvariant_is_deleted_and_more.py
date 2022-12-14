# Generated by Django 4.1.2 on 2022-11-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0008_remove_productimage_user_productimage_product_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productvariantvalue",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="productvariantvalue",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
