# Generated by Django 4.1.3 on 2022-11-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0009_pet_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='age',
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(default='Desconocido', max_length=6),
        ),
    ]