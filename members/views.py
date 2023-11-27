from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Competitor, Judge, Teacher

def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'members/homepage.html')

def competitors_list(request: HttpRequest) -> HttpResponse:
    competitors = Competitor.objects.all()
    return render(request, 'members/competitors/list.html', dict(competitors=competitors))