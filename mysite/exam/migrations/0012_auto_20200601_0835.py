# Generated by Django 3.0.6 on 2020-06-01 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20200531_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='duration',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='exam',
            name='logtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 8, 34, 59, 719357)),
        ),
    ]
