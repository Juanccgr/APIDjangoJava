# Generated by Django 4.1.2 on 2023-03-02 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("veterinary", "0025_alter_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]
