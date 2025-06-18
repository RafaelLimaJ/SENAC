import time
BALA = 0.50
CHOCOLATE = 3.00
BISCOITO = 3.50
PIRULITO = 2.00
TOTAL = 0.00
while True:
    print("Bem vindo a Nossa Loja De Doces!!!")
    print("==============PREÇOS==============")
    print("1-BALA = 0,50")
    print("2-CHOCOLATE = 3,00")
    print("3-BISCOITO = 3,50")
    print("4-PIRULITO = 2,00")
    print("5-FINALIZAR COMPRA")
    print("O seu valor R$",TOTAL)
    print("==================================")
    
    
    Escolha = input("Por favor digite os numeros dos Doces")
    if Escolha == "1":
        Quantidade1 = int(input("Quantas Balas você gostaria?"))
        subtotal = Quantidade1*BALA
        TOTAL += subtotal

    elif Escolha == "2":
        Quantidade2 = int(input("Quantos Chocolates você gostaria?"))
        subtotal = Quantidade2 * CHOCOLATE
        TOTAL += subtotal

    elif Escolha == "3":
        Quantidade3 = int(input("Quantos Biscoitos você gostaria?"))
        subtotal = Quantidade3 * BISCOITO
        TOTAL += subtotal

    elif Escolha == "4":
        Quantidade4 = int(input("Quantos Pirulitos você gostaria?"))
        subtotal = Quantidade4 * PIRULITO
        TOTAL += subtotal
    elif Escolha == "5":
        print("Obrigado Pela compra!!!!")
        time.sleep (3)
        break
