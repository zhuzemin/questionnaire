# Generated by Django 3.0.6 on 2020-06-01 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_auto_20200601_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='logtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 10, 47, 55, 484167)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='userAnswer',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
