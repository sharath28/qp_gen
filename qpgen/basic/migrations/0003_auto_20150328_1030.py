# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20150318_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='subquestion',
            old_name='question_difficulty',
            new_name='difficulty',
        ),
        migrations.RenameField(
            model_name='subquestion',
            old_name='question_marks',
            new_name='marks',
        ),
        migrations.RemoveField(
            model_name='questionpaper',
            name='main_question',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='subquestion',
            name='question_text',
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='main_questions',
            field=models.ManyToManyField(to='basic.MainQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 3, 28, 10, 29, 25, 575986), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subquestion',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 3, 28, 10, 29, 43, 372), upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subquestion',
            name='text',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='date_of_exam',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
