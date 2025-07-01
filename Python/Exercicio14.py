while True:
    num1 = int(input("Primeiro Numero"))
    num2 = int(input("Segundo Numero"))
    num3 = int(input("Terceiro Numero"))
    numero = num1
    if numero < num2:
        numero = num2
    if numero < num3:
        numero = num3
    print (f"O maior numero é {numero}")