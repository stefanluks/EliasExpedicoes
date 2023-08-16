from django.shortcuts import render, redirect
from .models import Experiencia, Pacote, Atrativo, Opcionais, AtrativoDia
from .forms import FormExperiencia, FormPacote, FormAtrativo, FormOpcionais, FormAtrativoDia

def Home(request):
    return render(request, "home.html", {
        "experiencias":Experiencia.objects.all(),
        "pacotes": Pacote.objects.all(),
    })
    
def Administracao(request):
    select = 'pct'
    if "select" in request.GET:
        select = request.GET['select']
    return render(request, 'adm.html', {
        "experiencias":Experiencia.objects.all(),
        "atrativos": list(Atrativo.objects.all()),
        'pacotes':list(Pacote.objects.all()),
        "opcionais": list(Opcionais.objects.all()),
        "atrativos_dias":list(AtrativoDia.objects.all()),
        'selecionado':select,
    })


def FormExp(request, id):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormExperiencia()
            return render(request, 'form.html', {"titulo":"Experiência",'form':form})
        elif request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")


def FormAtrd(request, id):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormAtrativoDia()
            return render(request, 'form.html', {"titulo":"Atrativo Dia",'form':form})
        elif request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
    
def FormAtr(request, id):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormAtrativo()
            return render(request, 'form.html', {"titulo":"Atrativo",'form':form})
        elif request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")

   
def FormPct(request, id):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormPacote()
            return render(request, 'form.html', {"titulo":"Pacotes",'form':form})
        elif request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
def FormOpc(request, id):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormOpcionais()
            return render(request, 'form.html', {"titulo":"Opicionais",'form':form})
        elif request.method == "POST":
            exp = Experiencia()
            exp.nome = request.POST["nome"]
            exp.capa = request.POST["capa"]
            exp.save()
            return redirect("Administracao")
    else:
        return redirect("login")