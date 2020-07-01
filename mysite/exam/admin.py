from django.contrib import admin
from mysite.exam.models import *


class quizAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'genre',)
    list_filter = ('genre',)


class answerAdmin(admin.ModelAdmin):
    list_display = ('name', 'correct',)


class intervieweeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class typeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class genreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class examAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'interviewee', 'logtime', 'status',)
    date_hierarchy = 'logtime'
    ordering = ('logtime',)
    search_fields = ('uuid', 'interviewee',)


admin.site.register(quiz, quizAdmin)
admin.site.register(exam, examAdmin)
admin.site.register(interviewee, intervieweeAdmin)
admin.site.register(answer, answerAdmin)
admin.site.register(type, typeAdmin)
admin.site.register(genre, genreAdmin)