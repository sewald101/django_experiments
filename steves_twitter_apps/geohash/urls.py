from django.urls import path

from . import views

app_name = 'geohash'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /geohash/2490383/tophash/
    path('<name>/', views.tophash, name='tophash'),
    path('<country>/<name>/', views.tophash, name='tophash'),
]
