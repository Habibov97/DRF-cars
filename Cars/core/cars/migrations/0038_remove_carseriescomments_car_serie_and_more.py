# Generated by Django 4.1.7 on 2023-03-16 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0037_carseriescomments_car_serie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carseriescomments',
            name='car_serie',
        ),
        migrations.AlterField(
            model_name='carseriescomments',
            name='modelnumbers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelnum', to='cars.carseries'),
        ),
    ]
