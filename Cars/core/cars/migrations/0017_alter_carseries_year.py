# Generated by Django 4.1.7 on 2023-03-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_alter_cars_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseries',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]