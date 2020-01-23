from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', include('headhot.urls')),
    path('', include('api.urls')),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('admin/', admin.site.urls),
]