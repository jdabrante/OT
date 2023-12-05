from django.urls import path

from . import views

app_name = 'competitors'

urlpatterns = [path('competitors/', views.competitors_list, name='competitors_list')]
