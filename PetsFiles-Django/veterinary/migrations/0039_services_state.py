# Generated by Django 4.1.7 on 2023-03-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("veterinary", "0038_remove_pet_estado"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="state",
            field=models.CharField(
                default="Activo", max_length=10, verbose_name="Estado"
            ),
        ),
    ]
