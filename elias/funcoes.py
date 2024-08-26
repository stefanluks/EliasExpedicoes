texto = """Almoço no Distrito de Taquaruçu
Almoço no Restaurante do Léo
Almoço no Restaurante do Adélio
Almoço no Restaurante do Fervedouro Por Enquanto
Cachoeira da Roncadeira
#Rapel opcional R$ 150,00 por pessoa ou Tirolesa opcional R$ 150,00 por pessoa
Cachoeira da Velha
Cachoeira das Araras
Cachoeira do Evilson
Cachoeira do Formiga
Dunas do Jalapão
Encontro dos Mirante da Serra do Espírito Santo / Morro do Saca Trapo / Árvore do Desejo / Recanto das Dunas (contemplação e fotos) Lagoa do Jacaré (contemplação e fotos)
Fervedouro Bela Vista
Fervedouro das Macaúbas
Fervedouro do Alecrim
Fervedouro do Buritizinho
Fervedouro do Ceiça
Fervedouro dos Buritis
Fervedouro Encontro das Águas
Fervedouro Por Enquanto
Lagoa do Japonês
Morro da Cachorra
#Opcional: Subida da Serra do Espírito Santo ou Morro do Sereno R$ 200,00 por pessoa ou subida do Morro do Jacurutu R$ 150,00 por pessoa
Parque Encantado
Pedra Furada
Prainha Coração do Jalapão
Prainha do Rio Novo Rios"""

from .models import Atrativo, Opcionais

lista = texto.split("\n")

def CallAuto():
    ant = None
    for atrativo in lista:
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