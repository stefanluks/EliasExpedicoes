from django.shortcuts import render, redirect
from .models import Experiencia, Pacote, Atrativo, Opcionais, AtrativoDia
from .forms import FormExperiencia, FormPacote, FormAtrativo, FormOpcionais, FormAtrativoDia

BTN_NOVO = {
    "pct":"Novo Pacote",
    "atr":"Novo Atrativo",
    "atrd":"Novo Atrativo por Dia",
    "opc":"Novo Opcional",
    "exp":"Nova Experiência",
}

def Home(request):
    return render(request, "home.html", {
        "experiencias":Experiencia.objects.all(),
        "pacotes": Pacote.objects.all(),
    })

  
def Administracao(request):
    if request.user.is_authenticated:
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
            "btnNovo":BTN_NOVO[select]
        })
    else:
        return redirect('login')


def FormExp(request, id):
    if request.user.is_superuser:
        exp = Experiencia.objects.get(pk=id)
        if request.method == "GET":
            exp = Experiencia.objects.get(pk=id)
            form = FormExperiencia(request.POST or None, instance=exp) 
            return render(request, 'form.html', {"titulo":"Experiência",'form':form})
        elif request.method == "POST":
            form = FormExperiencia(request.POST or None, instance=exp) 
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")


def FormAtrd(request, id):
    if request.user.is_superuser:
        atrd = AtrativoDia.objects.get(pk=id)
        if request.method == "GET":
            form = FormAtrativoDia(request.POST or None, instance=atrd) 
            return render(request, 'form.html', {"titulo":"Atrativo Dia",'form':form})
        elif request.method == "POST":
            form = FormAtrativoDia(request.POST or None, instance=atrd) 
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
    
def FormAtr(request, id):
    if request.user.is_superuser:
        atv = Atrativo.objects.get(pk=id)
        if request.method == "GET":
            form = FormAtrativo(request.POST or None, instance=atv)
            return render(request, 'form.html', {"titulo":"Atrativo",'form':form})
        elif request.method == "POST":
            form = FormAtrativo(request.POST or None, instance=atv)
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")

   
def FormPct(request, id):
    if request.user.is_superuser:
        pct = Pacote.objects.get(pk=id)
        if request.method == "GET":
            form = FormPacote(request.POST or None, instance=pct)
            return render(request, 'form.html', {"titulo":"Pacotes",'form':form})
        elif request.method == "POST":
            form = FormPacote(request.POST or None, instance=pct)
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
   
def FormOpc(request, id):
    if request.user.is_superuser:
        opc = Opcionais.objects.get(pk=id)
        if request.method == "GET":
            form = FormOpcionais(request.POST or None, instance=opc)
            return render(request, 'form.html', {"titulo":"Opicionais",'form':form})
        elif request.method == "POST":
            form = FormOpcionais(request.POST or None, instance=opc)
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")
  
    
def ExcExp(request, id):
    if request.is_authenticated:
        if Experiencia.objects.filter(pk=id):
            item = Experiencia.objects.get(pk=id)
            item.delete()
        return redirect("adm")
    else:
        return redirect("login")
    
    
def ExcPct(request, id):
    if request.is_authenticated:
        if Pacote.objects.filter(pk=id):
            item = Pacote.objects.get(pk=id)
            item.delete()
        return redirect("adm")
    else:
        return redirect("login")
    
    
def ExcAtr(request, id):
    if request.is_authenticated:
        if Atrativo.objects.filter(pk=id):
            item = Atrativo.objects.get(pk=id)
            item.delete()
        return redirect("adm")
    else:
        return redirect("login")


def ExcAtrd(request, id):
    if request.is_authenticated:
        if AtrativoDia.objects.filter(pk=id):
            item = AtrativoDia.objects.get(pk=id)
            item.delete()
        return redirect("adm")
    else:
        return redirect("login")
    
    
def ExcOpc(request, id):
    if request.is_authenticated:
        if Opcionais.objects.filter(pk=id):
            item = Opcionais.objects.get(pk=id)
            item.delete()
        return redirect("adm")
    else:
        return redirect("login")
    
    
def PctView(request, id):
    if request.user.is_authenticated:
        return render(request, 'Pacote.html', {
            'pacote': Pacote.objects.get(pk=id)
        })
    else:
        return redirect("login")