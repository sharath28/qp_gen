from django.db import models
from flufl.enum import IntEnum

class DifficultTypeEnum(IntEnum):
	unknown = 0
	easy = 1
	medium = 2
	hard = 3


class Subject(models.Model):
	name		= models.CharField(max_length=200)
	code		= models.CharField(max_length=10)
	semester	= models.IntegerField()
	branch		= models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Question(models.Model):

	DIFFICULTY_TYPES = [ (int(enum_choice), enum_choice.name) for enum_choice in DifficultyTypeEnum ]

	text		  = models.CharField(max_length=500)
	marks		  = models.IntegerField(default=0)
	subject 	  = models.ForeignKey('Subject')
	difficulty	  = models.IntegerField(default=int(DifficultyTypeEnum.unknown), choices=DIFFICULTY_TYPES)
	unit		  = models.IntegerField()
	created_at	  = models.DateTimeField(auto_now_add=True, null=False, editable=False)
	updated_at	  = models.DateTimeField(auto_now=True, null=False, editable=False)

	def __str__(self):
		return self.subject.name


class QuestionImage(models.Model):
	question	= models.ForeignKey('Question')
	caption		= models.CharField(max_length=200, blank=True)
	image		= models.ImageField(upload_to='question_images')


class MainQuestion(models.Model):
	question_no	  = models.PositiveIntegerField()
	sub_questions = models.ManyToManyField('Question')


class QuestionPaper(models.Model):
	university		= models.CharField(max_length=200)
	subject 		= models.ForeignKey(Subject)
	main_questions	= models.ManyToManyField('MainQuestion')
	max_marks		= models.IntegerField(default=0)
	date_of_exam	= models.DateField()
	teacher_name	= models.CharField(max_length=30)
	created_at		= models.DateTimeField(auto_now_add=True, null=False, editable=False)
	updated_at		= models.DateTimeField(auto_now=True, null=False, editable=False)

	def __str__(self):
		semester = self.subject.semester
		subject_name = self.subject.name

		return "#{} [Sem {}] {}".format(self.pk,semester,subject_name)
