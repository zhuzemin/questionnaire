# Generated by Django 3.0.6 on 2020-05-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20200527_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]