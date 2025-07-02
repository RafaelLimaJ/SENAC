contador = int(input("Digite seu numero"))
for contador in range (1, contador+1):
    resultado = contador % 2
    if resultado == 0:
        print (contador)