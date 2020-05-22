from django.urls import path

from . import views

app_name = 'geohash'

urlpatterns = [
    path('', views.index, name='index'),
    path('<name>/', views.tophash, name='tophash_name'),
    path('<country>/<name>/', views.tophash, name='tophash'),
    path('<country>/', views.tophash, name='tophash_country'),
]
