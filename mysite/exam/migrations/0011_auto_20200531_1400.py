# Generated by Django 3.0.6 on 2020-05-31 06:00

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20200529_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='duration',
        ),
        migrations.AlterField(
            model_name='exam',
            name='logtime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 14, 0, 13, 622433)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='userAnswer',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
