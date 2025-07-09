while True:
    try:
        num1 = int(input("Digite um numero"))
        num2 = int(input("Digite um numero"))

        conta = num1 + num2
        print (conta)
        break
    except ValueError:
        print("Valor Invalido")
