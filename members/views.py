from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Competitor, Judge, Teacher


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'members/homepage.html')


def competitors_list(request: HttpRequest) -> HttpResponse:
    competitors = Competitor.objects.all()
    return render(request, 'members/competitors/list.html', dict(competitors=competitors))


def teachers_list(request: HttpRequest) -> HttpResponse:
    teachers = Teacher.objects.all()
    return render(request, 'teachers/list.html', dict(teachers=teachers))


def judge_list(request: HttpRequest) -> HttpResponse:
    judge = Judge.objects.all()
    return render(request, 'judge/list.html', dict(judge=judge))
