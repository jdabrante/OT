from django.urls import path

from . import views

app_name = 'competitors'

urlpatterns = [
    path('competitors/', views.competitors_list, name='competitors_list'),
    path('competitors/<slug:competitor_slug>/', views.competitor_detail, name='competitor_detail'),
    ]
