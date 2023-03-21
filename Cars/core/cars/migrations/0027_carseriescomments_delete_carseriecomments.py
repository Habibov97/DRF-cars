# Generated by Django 4.1.7 on 2023-03-16 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0026_carseriecomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSeriesComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('modelnumbers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modelnum', to='cars.carseries')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.DeleteModel(
            name='CarSerieComments',
        ),
    ]
