from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def resultado(request):
    escolha_usuario = request.POST.get('jogada')
    opcoes = ['🪨', '📄', '✂️']
    random_jogada = random.choice(opcoes)
    if escolha_usuario == random_jogada:
        resultado = 'Empate!'
    elif escolha_usuario == '🪨' and random_jogada == '✂️':
        resultado = 'Você ganhou!'
    elif escolha_usuario == '📄' and random_jogada == '🪨':
        resultado = 'Você ganhou!'
    elif escolha_usuario == '✂️' and random_jogada == '📄':
        resultado = 'Você ganhou!'
    else:
        resultado = 'Você perdeu!'
    
    
    contexto = {
        'escolha_usuario': escolha_usuario,
        'random_jogada': random_jogada,
        'resultado': resultado
    }
    
    

    return render(request, 'resultado.html', contexto)
