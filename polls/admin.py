from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pubdate', 'question_text']
	
admin.site.register(Question, QuestionAdmin)

