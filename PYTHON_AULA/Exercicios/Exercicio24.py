lista = []
while True:
    print("Para remover algum item digite (remover) ")
    mercado = input("Digite oque deseja adicionar na lista: ")
    lista.append(mercado)
    
    
    if mercado == "remover":
        remover = input("DIGITE EXATAMENTE DO MESMO JEITO DA PALAVRA QUE DESEJA REMOVER")
        lista.remove(remover)
        lista.remove("remover")

    for item in lista:
        print (item)
