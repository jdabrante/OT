from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'subject']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
