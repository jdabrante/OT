from django.shortcuts import render, get_object_or_404
from .models import Teacher
from django.http import HttpRequest, HttpResponse
from competitors.forms import SearchForm

def teachers_list(request: HttpRequest) -> HttpResponse:
    teachers = Teacher.objects.all()
    form = SearchForm()
    return render(request, 'teachers/list.html', dict(teachers=teachers, form=form, section='teachers'))

def  teacher_detail(request: HttpRequest, teacher_slug: str) -> HttpResponse:
    teacher = get_object_or_404(Teacher, slug=teacher_slug)
    form = SearchForm()
    return render(request, 'teachers/detail.html', dict(teacher=teacher, form=form, section='teachers'))
