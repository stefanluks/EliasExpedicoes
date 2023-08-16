from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Home, Administracao, FormExp, FormAtr, FormAtrd, FormPct, FormOpc

urlpatterns = [
    path('', Home, name="Home"),
    path('adm/', Administracao, name="Administracao"),
    path('FormExp/<int:id>', FormExp, name="FormExp"),
    path('FormPct/<int:id>', FormPct, name="FormPct"),
    path('FormAtr/<int:id>', FormAtr, name="FormAtr"),
    path('FormAtrd/<int:id>', FormAtrd, name="FormAtrd"),
    path('FormOpc/<int:id>', FormOpc, name="FormOpc"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
