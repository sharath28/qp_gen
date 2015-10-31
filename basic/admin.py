from django.contrib import admin
from basic.models import Question, QuestionImage, Subject, QuestionPaper, MainQuestion


class QuestionImageInline(admin.StackedInline):
    model = QuestionImage
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [QuestionImageInline]
	list_display = ('subject__name','text','marks','difficulty')

class SubjectAdmin(admin.ModelAdmin):
	search_fields = ('name','code')
	list_display = ('name','code','semester')

class MainQuestionAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]

class QuestionPaperAdmin(admin.ModelAdmin):
	search_fields = ('subject','teacher_name')
	list_display = ('date_of_exam','subject','max_marks','teacher_name','created_at')

admin.site.register(Question)
admin.site.register(QuestionImage)
admin.site.register(Subject)
admin.site.register(QuestionPaper)
admin.site.register(MainQuestion)
