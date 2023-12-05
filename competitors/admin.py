from django.contrib import admin

from .models import Competitor, MusicStyle


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    raw_id_fields = ['music_styles']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


@admin.register(MusicStyle)
class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}
