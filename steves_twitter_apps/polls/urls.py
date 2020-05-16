from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


"""  OLD CODE FIRST PART OF TUTORIAL
urlpatterns = [
    # ex: /polls/
    path('', views.index_2, name='index'),
    
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results_2, name='results'),
    
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
