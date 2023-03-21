# Generated by Django 4.1.7 on 2023-03-17 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0039_remove_carseriescomments_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carseries',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.cars', verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='carseries',
            name='modelnumber',
            field=models.CharField(max_length=100, verbose_name='Car Complect'),
        ),
        migrations.AlterField(
            model_name='carseriescomments',
            name='modelnumbers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelnum', to='cars.carseries', verbose_name='Car Model'),
        ),
    ]