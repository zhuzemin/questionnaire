# Generated by Django 3.0.6 on 2020-05-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_answer_exam_genre_interviewee_quiz_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='quiz',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='name',
        ),
    ]
