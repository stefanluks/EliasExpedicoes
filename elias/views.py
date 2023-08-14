from django.shortcuts import render, redirect
from .models import Experiencia, Pacote, Atrativo

def Home(request):
    return render(request, "home.html", {
        "experiencias":Experiencia.objects.all(),
    })
    
def Administracao(request):
    select = 'pct'
    if "select" in request.GET:
        select = request.GET['select']
    return render(request, 'adm.html', {
        "experiencias":Experiencia.objects.all(),
        "atrativos": list(Atrativo.objects.all()),
        'pacotes':list(Pacote.objects.all()),
        'selecionado':select,
    })
    
def AddExp(request):
    if request.user.is_superuser:
        if request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")