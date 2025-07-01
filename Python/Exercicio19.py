import random

possiveis_escolhas = ["pedra","papel","tesoura"]
computador = random.choice(possiveis_escolhas)
print(computador)
escolha = input("(1) Pedra - (2) Papel - (3) Tesoura")

escolha = escolha.lower()
computador = computador.lower()


if computador == escolha:
    print ("Empate")
elif escolha == "pedra":
    if computador == "tesoura":
        print("Ganhou")
elif escolha == "Tesoura":
    if computador == "papel":
        print("Ganhou")          
elif escolha == "papel":
    print ("Ganhou")     
else:
    print ("Perdeu")
        
