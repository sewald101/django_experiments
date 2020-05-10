from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render

import json
import numpy as np
import pandas as pd
import os

from .models import Question, Woeids

from .top_bygeo import trending_by_geo

# pick this up later
# with open('/Users/sewald101/django_lab/twitter_experiments/steves_twitter_apps/geohash/woeids.json') as d:
#     woeids = json.load(d)

# Create your views here.
def index(request):
    return HttpResponse("This is Steve's experimental web site.")

def tophash(request, name='', country=''):
    country = country.title()
    name = name.title()
    if not country: # For worldwide
        querySet = (
        Woeids.objects.filter(name = name).values('woeid')
        )
    else: # For country, city
        querySet = (
        Woeids.objects.filter(name = name).filter(country = country).values('woeid')
        )
    woeid = querySet[0]['woeid']
    top_hashes = trending_by_geo(woeid=woeid)
    return render(request, "geohash/result.html", {'d': top_hashes})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "geohash/detail.html", {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def tophashes(request, name):
#     results = trending_by_geo(name).to_html()
#     return HttpResponse(results)
