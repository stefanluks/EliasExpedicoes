from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("elias.urls")),
    path('admin/', admin.site.urls),
    path('Conta/',include('django.contrib.auth.urls')),
]
