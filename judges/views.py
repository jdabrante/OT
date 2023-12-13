from django.shortcuts import render
from .models import Judge
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from competitors.forms import SearchForm

def judges_list(request: HttpRequest) -> HttpResponse:
    judges = Judge.objects.all()
    form = SearchForm()
    return render(request, 'judges/list.html', dict(judges=judges, form=form, section='judges'))

def judge_detail(request: HttpRequest, judge_slug: str) -> HttpResponse:
    judge = get_object_or_404(Judge, slug=judge_slug)
    form = SearchForm()
    return render(request, 'judges/detail.html', dict(judge=judge, form=form, section='judges'))