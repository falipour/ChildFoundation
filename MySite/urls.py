from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
    # TODO
    # path('hamyar/', include('hamyar.urls', namespace="hamyar")),
    # path('madadju/', include('madadju.urls', namespace="madadju")),
    # path('madadkar/', include('hamyar.urls', namespace="madadkar")),
    path('modir/', include('modir.urls'), name='modir'),
    path('', home, name='home'),
    path('', chart, name='chart'),
]
