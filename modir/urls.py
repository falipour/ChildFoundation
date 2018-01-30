from django.urls import path
from .views import *

urlpatterns = [
    path('goals/', AdminGoalsView.as_view()),
]


