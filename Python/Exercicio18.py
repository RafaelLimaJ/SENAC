
import random

numero = random.randint(1,10)
escolha = int(input("Diga seu numero"))
print("Adivinhe o numero entre 0 - 10")

    
while escolha != numero:
    escolha = int(input("Diga seu numero"))
    if escolha == numero:
        print ("GANHOU")
    else:
        print ("PERDEU")