from django.urls import path
from . import views
app_name = 'teachers'

urlpatterns = [
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('teachers/<slug:teacher_slug>', views.teacher_detail, name='teacher_detail')
]
