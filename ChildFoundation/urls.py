from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('karbar.urls')),
    # path('hamyar/', include('hamyar.urls')),
    # path('madadju/', include('madadju.urls')),
    # path('madadkar/', include('madadkar.urls')),
    path('modir/', include('modir.urls')),
]
