from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Home, Administracao, GerarPacotes, AddListAtrativos, View, FormExp, FormAtr, FormAtrd, FormPct, FormOpc, ExcExp, ExcPct, ExcAtr, ExcAtrd, ExcOpc, RoteiroView, PctInExp

urlpatterns = [
    path('', Home, name="Home"),
    path('adm/', Administracao, name="Administracao"),
    # path('gerarPacotes/', GerarPacotes, name="GerarPacotes"),
    path('View/<str:model>/<int:id>', View, name="View"),
    #----------- ADD new model -------------------
    path('FormExp/', FormExp, name="FormExp"),
    path('FormPct/', FormPct, name="FormPct"),
    path('FormAtr/', FormAtr, name="FormAtr"),
    path('FormAtrd/', FormAtrd, name="FormAtrd"),
    path('FormOpc/', FormOpc, name="FormOpc"),
    #------------- View model -------------
    path('FormOpc/', FormOpc, name="FormOpc"),
    path('ExcExp/<int:id>', ExcExp, name="ExcExp"),
    path('ExcPct/<int:id>', ExcPct, name="ExcPct"),
    path('ExcAtr/<int:id>', ExcAtr, name="ExcAtr"),
    path('ExcAtrd/<int:id>', ExcAtrd, name="ExcAtrd"),
    path('ExcOpc/<int:id>', ExcOpc, name="ExcOpc"),
    path('RoteiroPage/<int:id>', RoteiroView, name="RoteiroPage"),
    #-------------  API --------------------------
    path('PctInExp/<int:id>', PctInExp, name="PctInExp"),
    path('AddListAtrativos/', AddListAtrativos, name="AddListAtrativos"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
