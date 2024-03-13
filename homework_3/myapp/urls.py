from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('last_week/', last_week, name='last_week'),
    path('last_month/', last_month, name='last_month'),
    path('last_year/', last_year, name='last_year'),    
    path('about/', about, name='about'), 
]