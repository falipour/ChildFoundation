from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('MySite.urls'), name='my-site'),
    path('admin/', admin.site.urls),
    path('madadju/',include('madadju.urls'),name='madadju'),
    path('madadkar/',include('madadkar.urls'),name='madadkar')
]
