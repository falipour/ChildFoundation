from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminHomeView.as_view(), name='admin-home'),
    path('goals/', AdminGoalsView.as_view(), name='admin-goals'),
    path('history/', AdminHistoryView.as_view(), name='admin-history'),
    path('chart/', AdminChartView.as_view(), name='admin-chart'),
    path('contact/', AdminContactView.as_view(), name='admin-contact'),
    # path('madadkar-register/', AdminMadadkarRegisterView.as_view(), name='admin-madadkar-register'),
    # path()
]
