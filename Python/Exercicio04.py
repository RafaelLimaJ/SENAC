import time
while True:
    print("Bem-Vindo a TABUADA")
    num1=int(input ("Escolha seu Primeiro Numero"))
    limite=int(input ("Escolha seu Segundo Numero"))
    
    for i in range (limite + 1):
        resultado = num1 * i
        print (f"Resultado={num1}x{i}={resultado}")
    recomeçar = input("Voce deseja fazer outra tabuada? (s/n)")
    if recomeçar != 's':    
        print ("Obrigado por usar nossa Tabuada")
        time.sleep (3)
        break
