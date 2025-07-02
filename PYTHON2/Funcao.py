def imc():
        while True:
            peso = float(input("Coloque seu peso\n"))
            altura = float(input("Coloque sua altura\n"))
            if altura:
                imc = peso / (altura * altura)
            if imc < 25:
                print(f"Seu Imc é {imc} você esta no peso ideal")
            else:
                print(f"Seu IMC é {imc} você esta acima do peso")
def par_impar():
        print("Numero Par ou Impar?")
        n = int(input("Escolhe ate qual numero você quer ver"))
        for i in range(n):
            i = i + 1
            if i % 2 == 0:
                print (f"{i} é par")
            else:
                print (f"{i} é Impar")
def calculadora_soma():
                num1 = int(input("Escolha seu numero"))
                num2 = int(input("Escolha seu numero"))
                conta = num1 + num2
                print (f"Resultado de {num1}+{num2} = {conta}")
def calculadora_subtraçao():
                num1 = int(input("Escolha seu numero"))
                num2 = int(input("Escolha seu numero"))
                conta = num1 - num2
                print (f"Resultado de {num1}-{num2} = {conta}")
def calculadora_multiplicaçao():
                num1 = int(input("Escolha seu numero"))
                num2 = int(input("Escolha seu numero"))
                conta2 = num1 * num2
                print (f"Resultado de {num1}*{num2} = {conta2}")
def calculadora_divisao():
        num1 = int(input("Escolha seu numero"))
        num2 = int(input("Escolha seu numero"))
        conta = num1 / num2
        print (f"Resultado de {num1}/{num2} = {conta}")
def calculadora_potencia():
        num1 = int(input("Escolha seu numero"))
        num2 = int(input("Escolha seu numero"))
        conta = num1 ** num2
        print (f"Resultado de {num1}^{num2} = {conta}")         
def calculadora():        
        print(f"Soma (1)\n""Subtraçao(2)\n""Multiplicaçao (3)\n""Divisao (4)\n""Potencia (5)")
        escolha = int(input("Escolha um numero de 1 - 4"))
        if escolha == 1:
            calculadora_soma()
        elif escolha == 2:
            calculadora_subtraçao()
        elif escolha == 3:
            calculadora_multiplicaçao()
        elif escolha == 4:
             calculadora_divisao()
        elif escolha == 5:
             calculadora_potencia()
def tabuada():
            print("Bem-vindo a tabuada")
            num1 = int(input("Qual seu numero"))
            num2 =int(input("Qual seu numero"))
            for i in range(1, num2+1):
                conta = num1 * i
                print(f"{num1} * {i} = {conta}")
def calculo_idade():
        num1 =int(input("Em que ano voce nasceu?"))
        num2 = int(input("Qual ano voce quer saber sua idade?"))
        conta = num2 - num1
        print (f"Voce tera em {num2} {conta} anos")
def sequencia():
         alcance = int(input("Digite ate qual numero voce deseja que a sequencia vá\n"))
         print(0)
         a = 0 
         b = 1
         while b < alcance:
            print (b)
            c = a
            a = b
            b = b + c
def celcius():
        escolha = int(input("Deseja converter de CELSIUS - FAHRENHEIT (1) / FAHRENHEIT - CELSIUS (2) "))
        if escolha == 2:
            fah = int(input("Digite quantos fahrenheit deseja converter para celsius?"))
            grau = (fah - 32)*5/9
            print(f"{fah} Fahrenheit é {grau} Celsius")
        if escolha == 1:
            grau = int(input("Digite quantos celsius deseja converter para fahrenheit"))
            fah = (grau*9/5) + 32
            print(f"{grau} celcius para fahreinheit é {fah}\n")       
def divisores():
    numero = int(input("Digite o numero que deseja ver os divisores Inteiros dele"))

    for i in range(1, numero+1):
        resultado = numero // i
        if numero % i == 0: 
            print(f"{numero} / {i} = {resultado}")
def km():
    print("Converter Kilometros (1) \n Converter Metros(2)\n Converter Centimetros (3) ")
    escolha = int(input("Escolha para converter as distancias (1 - 3)"))
    
    if escolha == 1: #Kilometros
        print("Converter Kilometros para metros, centimetros e milimetros")
        kilometros = int(input("Digite quantos Kilometros deseja converter"))
        conta = kilometros * 1000
        conta1 = kilometros * 10000
        conta2 = kilometros * 100000
        print(f"{conta} Metros\n {conta1} Centimetros\n {conta2} Milimetros")
    if escolha == 2: #Metros 
          print("Converter Metros para Kilometros, Centimetros e Milimetros")
          metros = int(input("Digite a quantidade de Metros para converter"))
          conta = metros / 1000
          conta1 = metros * 100
          conta2 = metros * 1000
          print(f"{conta} Kilometros\n {conta1} Centimetros\n {conta2} Milimetros")
    if escolha == 3: #centimetros
          print("Converter Centimetros para Metros e Milimetros")
          centimetros = int(input("Digite a quantidade de Centimetros para converter"))
          metro = centimetros / 100
          milimetro = centimetros * 10
          print(f"{metro} metros\n {milimetro} Milimetros")     