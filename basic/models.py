from django.db import models

class Subject(models.Model):
	name		= models.CharField(max_length=200)
	code		= models.CharField(max_length=10)
	semester	= models.IntegerField()
	branch		= models.CharField(max_length=10)

	def __str__(self):
		return self.name


class SubQuestion(models.Model):
	text		  = models.CharField(max_length=500)
	marks		  = models.IntegerField(default=0)
	subject 	  = models.ForeignKey(Subject)
	image 		  = models.ImageField(max_length=100)
	difficulty	  = models.CharField(max_length=10)
	section 	  = models.CharField(max_length=5)

	def __str__(self):
		return self.subject.name


class MainQuestion(models.Model):
	subquestions = models.ManyToManyField(SubQuestion)


class QuestionPaper(models.Model):
	university		= models.CharField(max_length=200)
	subject 		= models.ForeignKey(Subject)
	mainquestions	= models.ManyToManyField(MainQuestion)
	max_marks		= models.IntegerField(default=0)
	date_of_exam	= models.DateField()
	teacher_name	= models.CharField(max_length=30)

	def __str__(self):
		semester = self.subject.semester
		subject_name = self.subject.name

		return "#{} [Sem {}] {}".format(self.pk,semester,subject_name) 

	def __str__(self):
		
		return ""
