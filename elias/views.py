import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .funcoes import CallAuto
from .models import Experiencia, Pacote, Atrativo, Opcionais, AtrativoDia, Roteiro
from .forms import FormExperiencia, FormPacote, FormAtrativo, FormOpcionais, FormAtrativoDia

BTN_NOVO = {
    "pct":"Novo Pacote",
    "atr":"Novo Atrativo",
    "atrd":"Novo Atrativo por Dia",
    "opc":"Novo Opcional",
    "exp":"Nova Experiência",
}

def Home(request):
    CallAuto()
    return render(request, "home.html", {
        "experiencias":Experiencia.objects.all(),
        "pacotes": Pacote.objects.all(),
        "roteiros":Roteiro.objects.filter(destaque=True)
    })

  
def Administracao(request):
    if request.user.is_authenticated:
        selecionado = None
        editando = False
        if 'edit' in request.GET:
            editando = request.GET["edit"]
        if "sel" in request.GET:
            selecionado = Pacote.objects.get(pk=int(request.GET["sel"]))
        return render(request, 'administracao.html', {
            "pacotes":list(Pacote.objects.all()),
            'selecionado':selecionado,
            'editando':editando,
            'experiencias':Experiencia.objects.all()
        })
    else:
        return redirect('login')



def FormExp(request):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormExperiencia()
            return render(request, 'form.html', {"titulo":"Experiência",'form':form})
        elif request.method == "POST":
            form = FormExperiencia(request.POST or None, instance=Experiencia()) 
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")


def FormAtrd(request):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormAtrativoDia() 
            return render(request, 'form.html', {"titulo":"Atrativo Dia",'form':form})
        elif request.method == "POST":
            form = FormAtrativoDia(request.POST or None, instance=AtrativoDia()) 
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
    
def FormAtr(request):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormAtrativo()
            return render(request, 'form.html', {"titulo":"Atrativo",'form':form})
        elif request.method == "POST":
            form = FormAtrativo(request.POST or None, instance=Atrativo())
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")

   
def FormPct(request):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormPacote()
            return render(request, 'form.html', {"titulo":"Pacotes",'form':form})
        elif request.method == "POST":
            form = FormPacote(request.POST or None, instance=Pacote())
            if form.is_valid():
                form.save()
            return redirect("Administracao")
    else:
        return redirect("login")
   
   
def FormOpc(request):
    if request.user.is_superuser:
        if request.method == "GET":
            form = FormOpcionais()
            return render(request, 'form.html', {"titulo":"Opicionais",'form':form})
        elif request.method == "POST":
            form = FormOpcionais(request.POST or None, instance=Opcionais())
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


def GetFormModel(modelo):
    if modelo == 'experiencias':
        return FormExperiencia()
    elif modelo == 'pacotes':
        return FormPacote()
    elif modelo == 'atrativos':
        return FormAtrativo()
    elif modelo == 'opicionais':
        return FormOpcionais()
    elif modelo == 'atrativos_dias':
        return FormAtrativoDia()

def View(request,model,id):
    if request.user.is_authenticated:
        form = GetFormModel(model)
        return render(request, 'form.html', {"titulo":model,'form':form})
    else:
        return redirect("login")
    


def ObjectMake(objeto):
    obj = {
        "id":objeto.id,
        "nome":objeto.nome,
        "descricao":objeto.descricao,
        "valor":objeto.valor,
        "limite":objeto.limite,
        "capa":"...",
        "atrativo_dias":[],
        "saida":objeto.saida,
        "volta":objeto.volta,
    }
    if objeto.capa:
        obj["capa"] = objeto.capa.url

    for at in objeto.atrativo_dias.all():
        obj["atrativo_dias"].append({
            "dia":at.dia,
            "atrativos":at.getAtrativos()
        })
    return obj


def PctInExp(request, id):
    pacotes = []
    if Experiencia.objects.filter(pk=id):
        experiencia = Experiencia.objects.get(pk=id)
        for p in list(Pacote.objects.all()):
            if experiencia in list(p.experiencias.all()):
                pacotes.append(p)
    saida = []
    for pct in pacotes:
        saida.append(ObjectMake(pct))
    return JsonResponse(data = saida, safe= False)


def RoteiroView(request, id):
    pacote = None
    if Pacote.objects.filter(pk=id):
        pacote = Pacote.objects.get(pk=id)
    return render(request, 'roteiro.html', {
        "pacote":pacote,
    })


def AddListAtrativos(request):
    if "lista" in request.GET:
        lista = request.GET["lista"]
        ant = None
        for atrativo in lista.split("\n"):
            if atrativo[0] != "#":
                a = Atrativo()
                a.nome = atrativo
                a.save()
                ant = a
            else:
                valor = atrativo.split("R$")[1].split(",00")[0]
                op = Opcionais()
                op.nome = atrativo
                op.valor = float(valor)
                op.save()
                ant.opcionais.add(op)
        return JsonResponse(data=True, safe=False)
    return JsonResponse(data=False, safe=False)


def GerarPacotes(request):
    if 'json' in request.GET:
        data = json.loads(request.GET["json"])
        for item in data:
            pct = Pacote()
            pct.nome = item["nome"]
            pct.descricao = item["descricao"]
            pct.valor = int(item["valor"])
            pct.limite = int(item["limite"])
            pct.save()
            filtro = ["nome","descricao","valor","limite","saida","volta","experiencias","capa","destacar"]
            for i in item:
                if i not in filtro:
                    if item[i] != None:
                        ad = AtrativoDia()
                        ad.dia = int(i)
                        ad.save()
                        for atrativo in item[i]:
                            a = Atrativo()
                            a.nome = atrativo
                            a.save()
                            ad.atrativos.add(a)
                        pct.atrativo_dias.add(ad)
            
        return JsonResponse(data=True, safe=False)
    return JsonResponse(data=False, safe=False)