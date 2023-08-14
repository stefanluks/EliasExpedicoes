from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Home, Administracao, AddExp

urlpatterns = [
    path('', Home, name="Home"),
    path('adm/', Administracao, name="Administracao"),
    path('AddExp', AddExp, name="AddExp"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
