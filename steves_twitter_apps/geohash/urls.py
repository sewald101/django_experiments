from django.urls import path

from . import views

app_name = 'geohash'

urlpatterns = [
    path('', views.index, name='index'),
    path('CountrySelect/', views.tophash_by_country, name='ByCountry'),
    path('MetroSelect/', views.tophash_by_metro, name='ByMetro'),
    path('m/<name>/', views.tophash, name='tophash_name'),
    path('m/<country>/<name>/', views.tophash, name='tophash'),
    path('m/<country>/', views.tophash, name='tophash_country'),
]
