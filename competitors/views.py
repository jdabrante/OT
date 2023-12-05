from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Competitor


def competitors_list(request: HttpRequest) -> HttpResponse:
    competitors = Competitor.objects.all()
    return render(request, 'competitors/list.html', dict(competitors=competitors))


def competitor_detaill(request: HttpRequest, competitor_slug: str) -> HttpResponse:
    competitor = get_object_or_404(Competitor, slug=competitor_slug)
    return render(request, 'competitors/detail.html', dict(competitor=competitor))
