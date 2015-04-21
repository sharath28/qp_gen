# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_marks', models.IntegerField(default=0)),
                ('date_of_exam', models.DateTimeField()),
                ('teacher_name', models.CharField(max_length=30)),
                ('main_question', models.ForeignKey(to='basic.MainQuestion')),
                ('subject', models.ForeignKey(to='basic.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('question_marks', models.IntegerField(default=0)),
                ('question_difficulty', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=5)),
                ('subject', models.ForeignKey(to='basic.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sub_question',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Sub_Question',
        ),
        migrations.AddField(
            model_name='mainquestion',
            name='sub_question',
            field=models.ForeignKey(to='basic.SubQuestion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_code',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
