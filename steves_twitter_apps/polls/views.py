from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

import json
import numpy as np
import pandas as pd
import os

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index_2.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results_2.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

""" OLD CODE EARLY IN TUTORIAL
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    title = ("Polls app -- Django official tutorial at: "
             "https://docs.djangoproject.com/en/3.0/"
    )
    invite = "Take a poll!"
    context = {'header':title, 
               'invite':invite,
               'questions':latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""
