from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Student)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_study_place', 'phone_number' )
    search_fields = ('name', )


@admin.register(Course)
class MentorAdmin(admin.ModelAdmin):
    list_filter = ('mentor__name', 'language__name')
    search_fields = ('mentor__name', 'student__name')
    list_display = ('name', 'date_started', 'mentor__name', 'student__name', 'language__name')


admin.site.register(Language)


