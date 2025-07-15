save = []

while True:    

    inventario = {
        "nome": "",
        "preço":"",
        "quantidade": "",
        "Preço_Total": ""
    }
    adicionar_nome = input("Digite o nome do produto")
    adicionar_preço = float(input("Digite o preço do produto"))
    adicionar_quantidade = int(input("Digite a quantidade do produto"))


    total = adicionar_preço * adicionar_quantidade

    inventario["nome"] = adicionar_nome
    inventario["preço"] = adicionar_preço
    inventario["quantidade"] = adicionar_quantidade
    inventario["Preço_Total"] = total
    save.append(inventario)
    for i in save:
        print(i)




