from django.db import models

# Create your models here.

class Sub_Question(models.Model):
	question_text=models.CharField(max_length=200)
	question_marks=models.IntegerField(default=0)
	subject=models.ForeignKey(Subject)
	#image=
	question_difficulty=model.CharField(max_length=10)
	#unit
	section=models.CharField(max_length=5)

class Subject(models.Model):
	subject_name=models.CharField(max_length=40)
	subject_code=models.CharField(max_length=6)
	semester=models.IntegerField(default=0)
	branch=models.CharField(max_length=10)

class Question_Paper():
	subject=models.ForeignKey(Subject)
	main_question=models.ForeignKey(Main_Question)
	max_marks=models.IntegerField(default=0)
	date_of_exam=models.DateField()
	teacher_name=models.CharField(max_length=30)

class Main_Question():
	sub_question=models.ForeignKey(Sub_Question)