
def soma():
    NUM1 = int(input("Digite o primeiro Numero"))
    NUM2 = int(input("Digite o segundo Numero"))
    total = NUM1 + NUM2
    print (f"O resultado de {NUM1} + {NUM2} = {total}")
def subtraçao():
    NUM1 = int(input("Digite o primeiro Numero"))
    NUM2 = int(input("Digite o segundo Numero"))
    total = NUM1 - NUM2
    print (f"O resultado de {NUM1} - {NUM2} = {total}")
def divisao():
    NUM1 = int(input("Digite o primeiro Numero"))
    NUM2 = int(input("Digite o segundo Numero"))
    total = NUM1 / NUM2
    print (f"O resultado de {NUM1} / {NUM2} = {total}")
def potencia():
    NUM1 = int(input("Digite o primeiro Numero"))
    NUM2 = int(input("Digite o segundo Numero"))
    total = NUM1 ** NUM2
    print (f"O resultado de {NUM1}^{NUM2} = {total}")    
def multiplicaçao():
    NUM1 = int(input("Digite o primeiro Numero"))
    NUM2 = int(input("Digite o segundo Numero"))
    total = NUM1 * NUM2
    print (f"O resultado de {NUM1} * {NUM2} = {total}")
def raiz():
    NUM1 = int(input("Digite o primeiro Numero"))
    total = NUM1 * 0.5
    print (f"O resultado de {NUM1} = {total}")
def radiano():
    PI=3.14
    NUM1 = float(input("Digite quantos graus voce deseja converter para radiano"))
    total = NUM1 * PI/180
    print (f"O resultado de {NUM1} PARA RADIANO É = {total}")
while True:
    print("\n 1-SOMA\n 2-SUBTRAÇAO\n 3-MULTIPLICAÇAO \n 4-DIVISAO\n 5-POTENCIA\n 6-RAIZ QUADRADA \n 7-GRAUS-RADIANO  \n 8-SAIR")
    Operador = input("Por favor escolha o numero do seu OPERADOR (1-8)")
    if Operador == "1":
        soma()
    elif Operador == "2":
       subtraçao()
    elif Operador == "3":
        multiplicaçao()
    elif Operador == "4":
      divisao()  
    elif Operador == "5":
       potencia()
    elif Operador == "6":
        raiz()
    elif Operador == "7":
        radiano()
    elif Operador == "8":
        break

    else:

        print ("OPERADOR INVALIDO")
        break