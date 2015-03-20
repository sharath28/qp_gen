from django.db import models
import datetime
# Create your models here.

class SubQuestion(models.Model):
	question_text=models.CharField(max_length=200)
	question_marks=models.IntegerField(default=0)
	subject=models.ForeignKey('Subject')
	#image=
	question_difficulty=models.CharField(max_length=10)
	#unit
	section=models.CharField(max_length=5)

class Subject(models.Model):
	subject_name=models.CharField(max_length=40)
	subject_code=models.CharField(max_length=10)
	semester=models.IntegerField(default=0)
	branch=models.CharField(max_length=10)

class QuestionPaper(models.Model):
	subject=models.ForeignKey('Subject')
	main_question=models.ForeignKey('MainQuestion')
	max_marks=models.IntegerField(default=0)
	date_of_exam=models.DateTimeField()
	teacher_name=models.CharField(max_length=30)

class MainQuestion(models.Model):
	sub_question=models.ForeignKey('SubQuestion')
