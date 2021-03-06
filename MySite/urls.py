from django.conf.urls import url, include
from django.urls import path
from .views import *
from karbar.views import login

urlpatterns = [
    # TODO
    # path('hamyar/', include('hamyar.urls', namespace="hamyar")),
    # path('madadju/', include('madadju.urls', namespace="madadju")),
    # path('madadkar/', include('hamyar.urls', namespace="madadkar")),
    path('modir/', include('modir.urls'), name='modir'),
    path('', home, name='home'),
    path('chart/', chart, name='chart'),
    path('goals/', goals, name='goals'),
    path('history/', history, name='history'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', login, name='login'),
    path('register/', HamyarView.as_view(), name='hamyar-register'),
]
