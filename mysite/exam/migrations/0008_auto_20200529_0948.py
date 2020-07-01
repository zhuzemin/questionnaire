# Generated by Django 3.0.6 on 2020-05-29 01:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_exam_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='finishTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='startTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='logtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]