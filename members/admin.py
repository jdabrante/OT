from django.contrib import admin
from .models import Competitor, Teacher, Judge

@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'music_style']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'job']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}