from django.conf.urls import url, include
from django.urls import path
from .views import *
import madadju

urlpatterns = [
    path('', madadju.views.madadjuhome, name='madadju-home'),
    path('goals/', madadju.views.madadjugoal, name='madadju-goals'),
    path('history/', madadju.views.madadjuhistory, name='madadju-history'),
    path('chart/', madadju.views.madadjuchart, name='madadju-chart'),
    path('contact/', madadju.views.madadjucontact, name='madadju-contact'),
    path('madadkar-change/', madadju.views.madadkarchange, name='madadju-madadkar-change'),
    path('profile/',madadju.views.madadjuprofile,name='madadju-profile'),
    path('sendmsg/',madadju.views.madadjumsg,name='madadju-msg'),
    path('sendreq/',madadju.views.madadjureq,name='madadju-req')
]
