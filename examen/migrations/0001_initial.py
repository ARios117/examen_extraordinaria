# Generated by Django 3.2.6 on 2022-06-16 13:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('anyoCompra', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['tipo', 'anyoCompra'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['nombre', 'edad'],
            },
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime(2022, 6, 16, 13, 39, 2, 987427, tzinfo=utc))),
                ('horaComienzo', models.IntegerField(default=0)),
                ('horaFin', models.IntegerField(default=0)),
                ('bicicleta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres', to='examen.bicicleta')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres', to='examen.cliente')),
            ],
            options={
                'ordering': ['bicicleta', 'cliente'],
            },
        ),
    ]
