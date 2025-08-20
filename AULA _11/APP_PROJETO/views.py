from django.shortcuts import render
import random


# Create your views here.
def home(request):


    NOMES = ["CARLOS", "MARIA", "JOÃO", "ANA", "PEDRO", "SOFIA", "LUCAS"]
    LOCAIS = ["A PADARIA", "O PARQUE", "A BIBLIOTECA", "O SUPERMERCADO", "A PRAIA", "A FLORESTA"]
    ITENS = ["UM MAPA DO TESOURO", "UMA CHAVE DOURADA", "UM LIVRO ANTIGO", "UM GATO MISTERIOSO", "UMA POÇÃO BRILHANTE"]
    ITENS2 = ["UMA CAIXA DE MADEIRA", "UMA MOCHILA VELHA", "UM BAÚ ESQUECIDO", "UMA GARRAFA DE VIDRO", "UM NINHO DE PÁSSARO"]

   
    nome_sorteado = random.choice(NOMES)
    local_sorteado = random.choice(LOCAIS)
    item_sorteado = random.choice(ITENS)
    item2_sorteado = random.choice(ITENS2)

    
    frase_final = f"{nome_sorteado} FOI ATE {local_sorteado} E ENCONTROU {item_sorteado} DENTRO DE {item2_sorteado}"

    

    return render(request, 'home.html',{'frase_final': frase_final})