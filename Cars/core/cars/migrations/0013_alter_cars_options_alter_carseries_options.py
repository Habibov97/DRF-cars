# Generated by Django 4.1.7 on 2023-03-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_rename_serienumber_carseries_modelnumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='carseries',
            options={'verbose_name_plural': 'Car series'},
        ),
    ]
