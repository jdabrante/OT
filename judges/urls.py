from django.urls import path
from . import views

app_name = 'judges'

urlpatterns = [
    path('judges/', views.judges_list, name='judge_list'),
    path('judges/<slug:judge_slug>/', views.judge_detail, name='judge_detail'),
]
