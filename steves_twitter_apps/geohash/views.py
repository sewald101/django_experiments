from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse

from .forms import SelectCountry

import json
import numpy as np
import pandas as pd
import os

from .models import Woeids

from .top_bygeo import trending_by_geo

# pick this up later
# with open('/Users/sewald101/django_lab/twitter_experiments/steves_twitter_apps/geohash/woeids.json') as d:
#     woeids = json.load(d)

# Create your views here.
def index(request):
    countries = Woeids.objects.values('country').distinct().order_by('country')
    ww = trending_by_geo(woeid=1)
    form = SelectCountry()
    context = {'countries': countries, 'd': ww, 'form':form}
    return render(request, 'geohash/index.html', context)

def tophash(request, name='', country=''):
    country = country.title()
    name = name.title()
    if not country: # For worldwide
        querySet = (
        Woeids.objects.filter(name = name).values('woeid')
        )
    elif not name: # For countries at country grain
        querySet = (
        Woeids.objects.filter(name = country).filter(country = country).values('woeid')
        )
    else: # For country, city
        querySet = (
        Woeids.objects.filter(name = name).filter(country = country).values('woeid')
        )
    woeid = querySet[0]['woeid']
    top_hashes = trending_by_geo(woeid=woeid)
    return render(request, "geohash/result.html", {'d': top_hashes})

