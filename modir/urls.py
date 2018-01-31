from django.urls import path
from .views import *

urlpatterns = [
    path('', HamyarHomeView.as_view(), name='hamyar-home'),
    path('goals/', HamyarGoalsView.as_view(), name='hamyar-goals'),
    path('history/', HamyarHistoryView.as_view(), name='hamyar-history'),
    path('chart/', HamyarChartView.as_view(), name='hamyar-chart'),
    path('contact/', HamyarContactView.as_view(), name='hamyar-contact'),
    path('enseraf/', EnserafView.as_view(), name='enseraf'),
    path('entekhab/', EntekhabView.as_view(), name='entekhab'),
    path('ehda/', EhdaView.as_view(), name='ehda'),
    path('letters/', LettersBoxView.as_view(), name='letters-box'),
]
