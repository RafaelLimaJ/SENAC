SALDO_INICIAL = 1000
Saldo=SALDO_INICIAL
while True:
    print("=======Caixa eletronico=======")
    print("1-Verificar Saldo")
    print("2-Depositar Valor")
    print("3-Sacar Valor")
    print("4-Sair")
    print("==============================")
        
    Escolha=(input("Escolha um numero de 1-4"))
        
    if Escolha == "1":
        print("Seu saldo é R$",Saldo)
            
    elif Escolha == "2":
        Valor=float(input("Qual valor você deseja Depositar?"))
        if Valor > 0:
            Saldo += Valor
            print ("Foi adicionado",Valor,"na sua conta")
        else:
            print ("Ação Invalida")
    elif Escolha == "3":
        Saque=float(input("Qual valor deseja sacar?"))
        if Saldo < Saque:
            print("Saldo Insuficiente")
        elif Saldo > Saque:
            Saldo -= Saque
    elif Escolha == "4":
        print("Obrigado por nos visitar!!")
        break
