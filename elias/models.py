from django.db import models


def AjusteMes(mes):
    if int(mes)< 10:
        return "0"+str(mes)
    return ""+mes


class Experiencia(models.Model):
    nome = models.CharField("Nome da Experiência", max_length=150)
    descricao = models.TextField("Descrição da Experiência", max_length=1500, null=True, blank=True)
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

    def getAtrativos(self):
        saida = ""
        for a in list(self.atrativos.all()):
            saida += a.nome + " - "
        return saida[:-2]
    
    def AtrativosExiste(self):
        return len(list(self.atrativos.all())) > 0
    
    def __str__(self):
        return "Atrativos do "+str(self.dia)+"º dia"


#pacote == ROTEIRO
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
    destacar = models.BooleanField("Destacar na página Inicial", default=False)
        
    def __str__(self):
        return self.nome
    
    def getValor(self):
        return int(self.valor)
    
    def getSaida(self):
        if self.saida:
            return f'{self.saida.year}-{AjusteMes(self.saida.month)}-{self.saida.day}'
        return None
    
    def getVolta(self):
        if self.volta:
            return f'{self.volta.year}-{AjusteMes(self.volta.month)}-{self.volta.day}'
        return None
    
    def QtdAtrativos(self):
        return len(list(self.atrativo_dias.all()))
    


class Roteiro(models.Model):
    class Meta:
        verbose_name = "ROTEIRO"
        verbose_name_plural = "ROTEIROS"

    nome = models.CharField("Nome do roteiro", max_length=150)
    imagem = models.FileField("Imagem com Atrativos", upload_to="static/imagens/", null=True, blank=True)
    destaque = models.BooleanField("Destacar na Página Inicial", default=False)
    dias = models.IntegerField("Quantidade de Dias", default=0)
    noites = models.IntegerField("Quantidade de Noites", default=0)

    def __str__(self) -> str:
        return self.nome