from django import forms
from .models import Experiencia, Pacote, Atrativo, Opcionais, AtrativoDia

class FormExperiencia(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = "__all__"
        
class FormPacote(forms.ModelForm):
    class Meta:
        model = Pacote
        fields = "__all__"

class FormAtrativo(forms.ModelForm):
    class Meta:
        model = Atrativo
        fields = "__all__"

class FormOpcionais(forms.ModelForm):
    class Meta:
        model = Opcionais
        fields = "__all__"

class FormAtrativoDia(forms.ModelForm):
    class Meta:
        model = AtrativoDia
        fields = "__all__"