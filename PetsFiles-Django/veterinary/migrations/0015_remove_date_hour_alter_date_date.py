# Generated by Django 4.1.3 on 2022-11-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0014_date_hour_alter_date_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='hour',
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
