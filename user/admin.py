from django.contrib import admin
from .models import *


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_work', 'phone_number', 'level')
    search_fields = ('name', )

    @admin.display(description='Level')
    def level(self, obj):
        today = datetime.date.today()
        c1 = today.year - 3
        c2 = today.month
        c3 = today.day
        new_date = datetime.date(year=c1, month=c2, day=c3)
        lv = new_date > obj.experience
        if lv:
            return 'Middle'
        else:
            return 'Strong Junior'


@admin.register(Student)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_study_place', 'phone_number' )
    search_fields = ('name', )


@admin.register(Course)
class MentorAdmin(admin.ModelAdmin):
    list_filter = ('mentor__name', 'language__name')
    search_fields = ('mentor__name', 'student__name')
    list_display = ('name', 'date_started', 'mentor', 'student', 'language', 'get_end_date')

    @admin.display(description='Date End')
    def get_end_date(self, obj):
        data = datetime.timedelta(days=obj.language.month_to_learn * 30)
        return obj.date_started + data


admin.site.register(Language)
