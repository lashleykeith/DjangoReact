# Generated by Django 2.0.5 on 2018-06-18 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2018, 6, 19, 0, 16, 28, 148629)),
        ),
    ]
