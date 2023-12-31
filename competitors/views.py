from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from .models import Competitor
from teachers.models import Teacher
from judges.models import Judge
from django.db.models import Q
from itertools import chain

def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard/dashboard.html')

def competitors_list(request: HttpRequest) -> HttpResponse:
    competitors = Competitor.objects.all()
    form = SearchForm()
    return render(request, 'competitors/list.html', dict(competitors=competitors, form=form, section='competitors'))


def competitor_detail(request: HttpRequest, competitor_slug: str) -> HttpResponse:
    competitor = get_object_or_404(Competitor, slug=competitor_slug)
    form = SearchForm()
    return render(request, 'competitors/detail.html', dict(competitor=competitor, form=form, section='competitors'))

def member_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query'].lower()
            competitors = set(Competitor.objects.annotate(search=SearchVector('first_name', 'last_name', 'birthdate', 'city', 'job', 'hobbies'))\
            .filter(Q(search=query) | Q(music_styles__name=query)))
            teachers = set(Teacher.objects.annotate(search=SearchVector('first_name', 'last_name', 'subject')).filter(search=query))
            judges = set(Judge.objects.annotate(search=SearchVector('first_name', 'last_name', 'job')).filter(search=query))    
            # Use chain to agrupate the 'querysets'
            results = chain(competitors, teachers, judges)
    return render(request, 'search.html', dict(results=results, form=form, query=query))