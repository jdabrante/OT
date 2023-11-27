from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('competitors/', views.competitors_list, name='competitors')
]
