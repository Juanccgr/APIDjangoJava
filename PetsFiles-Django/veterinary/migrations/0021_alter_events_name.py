# Generated by Django 4.1.3 on 2022-11-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0020_alter_events_client_alter_events_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(blank=True, default='Consulta', max_length=255, null=True),
        ),
    ]
