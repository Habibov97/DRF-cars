# Generated by Django 4.1.7 on 2023-03-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_remove_cars_active_carseries_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseries',
            name='active',
            field=models.BooleanField(),
        ),
    ]
