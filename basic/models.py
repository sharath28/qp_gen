from django.db import models

class SubQuestion(models.Model):
	text		= models.CharField(max_length=500)
	marks		= models.IntegerField(default=0)
	subject 	= models.ForeignKey('Subject')
	image 		= models.ImageField(max_length=100)
	difficulty	= models.CharField(max_length=10)
	section 	= models.CharField(max_length=5)

	def __str__(self):
		return self.subject.name

class Subject(models.Model):
	name		= models.CharField(max_length=200)
	code		= models.CharField(max_length=10)
	semester	= models.IntegerField()
	branch		= models.CharField(max_length=10)

	def __str__(self):
		return self.name

class QuestionPaper(models.Model):
	subject 		= models.ForeignKey('Subject')
	main_questions	= models.ManyToManyField('MainQuestion')
	max_marks		= models.IntegerField(default=0)
	date_of_exam	= models.DateField()
	teacher_name	= models.CharField(max_length=30)

	def __str__(self):
		return self.subject.name

class MainQuestion(models.Model):
	sub_question	= models.ForeignKey('SubQuestion')

	def __str__(self):
		return self.sub_question.text
