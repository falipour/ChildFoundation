from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('hamyar/', include('hamyar.urls', namespace="hamyar")),
    path('madadju/', include('madadju.urls', namespace="madadju")),
    path('madadkar/', include('hamyar.urls', namespace="madadkar")),
    path('modir/', include('hamyar.urls', namespace="modir")),
]
