from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
    path('', madadjuhome, name='madadju-home'),
    path('goals/', madadjugoal, name='madadju-goals'),
    path('history/', madadjuhistory, name='madadju-history'),
    path('chart/', madadjuchart, name='madadju-chart'),
    path('contact/', madadjucontact, name='madadju-contact'),
    path('madadkar-change/', madadkarchange, name='madadju-madadkar-change'),
    path('profile',madadjuprofile,name='madadju-profile')
]
