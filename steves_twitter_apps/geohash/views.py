from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render

import json
import numpy as np
import pandas as pd
import os

from .models import Question

# pick this up later
# with open('/Users/sewald101/django_lab/twitter_experiments/steves_twitter_apps/geohash/woeids.json') as d:
#     woeids = json.load(d)

# Create your views here.
def index(request):
    # latest_question_list = Question.objects.order_by('pub_date')[:5]
    # template = loader.get_template('geohash/table_test.html')
    # context = dict(
    #         df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
    # )
    result_values = [["X \u00c6 A-12",1144779],["Adele",611306],["Grimes",437021],["#8YearsWithRos\u00e9",381486],["Cinco de Mayo",329002],["#2YearsWithSingularity",152986],["Bundesliga",89333],["#ExposeCBS",88124],["#GivingTuesdayNow",83375],["#Chromatica",82896],["#NationalNursesDay",53308],["#WednesdayWisdom",41400],["#igot7selcaday",40421],["Kraftwerk",34520],["Robocop",20458],["Marsha",18924],["#JusticeForAhmaud",18299],["Sarah Paulson",14297],["#HandsOffMyBC",11120]]    # result =
    result_split = {"columns":["HashTag","TweetVol"],"index":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],"data":[["X \u00c6 A-12",1144779],["Adele",611306],["Grimes",437021],["#8YearsWithRos\u00e9",381486],["Cinco de Mayo",329002],["#2YearsWithSingularity",152986],["Bundesliga",89333],["#ExposeCBS",88124],["#GivingTuesdayNow",83375],["#Chromatica",82896],["#NationalNursesDay",53308],["#WednesdayWisdom",41400],["#igot7selcaday",40421],["Kraftwerk",34520],["Robocop",20458],["Marsha",18924],["#JusticeForAhmaud",18299],["Sarah Paulson",14297],["#HandsOffMyBC",11120]]}
    result_index = {"1":{"HashTag":"X \u00c6 A-12","TweetVol":1144779},"2":{"HashTag":"Adele","TweetVol":611306},"3":{"HashTag":"Grimes","TweetVol":437021},"4":{"HashTag":"#8YearsWithRos\u00e9","TweetVol":381486},"5":{"HashTag":"Cinco de Mayo","TweetVol":329002},"6":{"HashTag":"#2YearsWithSingularity","TweetVol":152986},"7":{"HashTag":"Bundesliga","TweetVol":89333},"8":{"HashTag":"#ExposeCBS","TweetVol":88124},"9":{"HashTag":"#GivingTuesdayNow","TweetVol":83375},"10":{"HashTag":"#Chromatica","TweetVol":82896},"11":{"HashTag":"#NationalNursesDay","TweetVol":53308},"12":{"HashTag":"#WednesdayWisdom","TweetVol":41400},"13":{"HashTag":"#igot7selcaday","TweetVol":40421},"14":{"HashTag":"Kraftwerk","TweetVol":34520},"15":{"HashTag":"Robocop","TweetVol":20458},"16":{"HashTag":"Marsha","TweetVol":18924},"17":{"HashTag":"#JusticeForAhmaud","TweetVol":18299},"18":{"HashTag":"Sarah Paulson","TweetVol":14297},"19":{"HashTag":"#HandsOffMyBC","TweetVol":11120}}
    # [pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['foo', 'bar', 'bazz']).to_json()]
    # print(result)
    # return HttpResponse(template.render(context, request))
    # return render(request, "geohash/table_test_02.html", {'d': result_values})
    # return render(request, "geohash/table_test_03.html", {'d': result_split})
    return render(request, "geohash/table_test_04.html", {'d': result_index})
    # return JsonResponse(result, safe=False)
    # return HttpResponse(result)

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
