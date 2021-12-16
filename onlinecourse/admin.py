from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson

class QuestionInline(admin.StackedInline):
    model = Question
    
class ChoiceInline(admin.StackedInline):
    model = Choice
    

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    fields = ['pub_date', 'name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course','question']
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_content']

class SubmissionAdmin(admin.ModelAdmin):
    
    fields = ['enrollment', 'choices']
    

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

admin.site.register(Submission, SubmissionAdmin)