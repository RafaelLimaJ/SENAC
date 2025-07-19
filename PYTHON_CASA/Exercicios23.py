while True:
    try:
        num1 = int(input("Digite o primeiro numero"))
        num2 = int(input("Digite o segundo numero"))

        conta1 = num1 + num2 
        conta2 = num1 - num2
        conta3 = num1 * num2
        conta4 = num1 / num2

        print(f"{num1} + {num2} = {conta1}\n{num1} - {num2} = {conta2}\n{num1} * {num2} = {conta3}\n {num1} / {num2} = {conta4}")
        break
    except ValueError:
        print("Digite apenas numeros")
    except ZeroDivisionError:
        print(f"{num1} + {num2} = {conta1}\n{num1} - {num2} = {conta2}\n{num1} * {num2} = {conta3}")
        print(f"Nao é possivel dividir {num1} por 0")