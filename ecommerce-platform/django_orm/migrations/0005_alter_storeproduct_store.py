# Generated by Django 4.2.4 on 2023-08-16 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("__main__", "0004_order_product_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storeproduct",
            name="store",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="__main__.store",
            ),
        ),
    ]
