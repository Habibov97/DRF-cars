# Generated by Django 4.1.7 on 2023-03-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_alter_carseries_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseries',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
