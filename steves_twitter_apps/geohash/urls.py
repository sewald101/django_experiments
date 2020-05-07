from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /geohash/2490383/tophash/
    path('<int:woeid>/tophash/', views.tophash, name='tophash'),
    # ex: /geohash/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /geohash/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /geohash/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # My stuff, ex: /geohash/seattle/
    # path('<str:name>', views.tophashes, name='tophashes')
]
