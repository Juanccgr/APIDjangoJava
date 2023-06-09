# Generated by Django 4.1.7 on 2023-03-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("veterinary", "0040_services_total_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="state",
            field=models.CharField(
                choices=[("Activo", "Activo"), ("Finalizado", "Finalizado")],
                default="Activo",
                max_length=10,
                verbose_name="Estado",
            ),
        ),
        migrations.AlterField(
            model_name="services",
            name="total_time",
            field=models.IntegerField(blank=True, null=True, verbose_name="Tiempo"),
        ),
    ]
