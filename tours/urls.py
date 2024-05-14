from django.urls import path,include
from . import views


urlpatterns = [
path('',views.tours,name='tours'),
path('showcity',views.showcity,name='showcity'),
path('destinations',views.destinations,name='destination'),
path('visited',views.visited,name='visited'),


]
    # path('tours',views.tours,name='tours'),