# Generated by Django 4.1.7 on 2023-03-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_cars_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='image',
        ),
        migrations.AddField(
            model_name='carseries',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
