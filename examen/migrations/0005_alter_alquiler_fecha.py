# Generated by Django 3.2.6 on 2022-06-16 13:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0004_auto_20220616_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 6, 16, 13, 51, 0, 169005, tzinfo=utc)),
        ),
    ]
