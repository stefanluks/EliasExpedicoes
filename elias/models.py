from django.db import models

class Experiencia(models.Model):
    nome = models.CharField("Nome da Experiência", max_length=150)
    atrativos = models.ManyToManyField("Atrativo", blank=True)
    capa = models.FileField("Imagem de Capa", upload_to="static/imagens/", null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    def getAtrativos(self):
        saida = ""
        for a in list(self.atrativos.all()):
            if a == list(self.atrativos.all())[-1]:
                saida += a.nome
            else:
                saida += a.nome + " - "
        return saida


class Opcionais(models.Model):
    nome = models.CharField("Nome do opcional", max_length=150)
    valor = models.FloatField("Valor do opcional", default=0)
    
    def __str__(self):
        return self.nome + " - R$ " + str(self.valor) +",00"


class Atrativo(models.Model):
    nome = models.CharField("Nome do atrativo", max_length=150)
    opcionais = models.ManyToManyField("Opcionais", blank=True)
    
    def __str__(self):
        return self.nome
    

class AtrativoDia(models.Model):
    dia = models.IntegerField("Dia do Pacote", default=1)
    atrativos = models.ManyToManyField("Atrativo", blank=True)


class Pacote(models.Model):
    nome = models.CharField("Nome do Pacote", max_length=150)
    descricao = models.TextField("Descrição do pacote", max_length=1500, blank=True, null=True)
    valor = models.FloatField("Valor do pacote (por pessoa)", default=0)
    limite = models.IntegerField("Minímo de turistas", default=4)
    atrativo_dias = models.ManyToManyField("AtrativoDia", blank=True)
    saida = models.DateField("Data de Saida", auto_now=False, auto_now_add=False, null=True, blank=True)
    volta = models.DateField("Data da volta", auto_now=False, auto_now_add=False, null=True, blank=True)
    experiencias = models.ManyToManyField(Experiencia, blank=True)
    capa = models.FileField("Imagem de Capa", upload_to="static/imagens/", null=True, blank=True)
        
    def __str__(self):
        return self.nome

