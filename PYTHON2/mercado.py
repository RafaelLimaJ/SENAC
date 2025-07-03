pirulito = 3.50
doces = 2.00
chocolate = 3.00
bala = 0.50
frutas = 1.50
legumes = 1.20

# Dicionário com os preços
precos = {
    "Pirulito": pirulito,
    "Doces": doces,
    "Chocolate": chocolate,
    "Bala": bala,
    "Frutas": frutas,
    "Legumes": legumes
}

carrinho = {}

while True:
    print("\nMercado")
    print("Preços:\n")
    print(f" (1) Pirulito: R$ {pirulito}")
    print(f" (2) Doces: R$ {doces}")
    print(f" (3) Chocolate: R$ {chocolate}")
    print(f" (4) Bala: R$ {bala}")
    print(f" (5) Frutas: R$ {frutas}")
    print(f" (6) Legumes: R$ {legumes}")
    print(" (7) Ver carrinho")

    escolha = input("Digite o número do que você quer comprar: ")

    if escolha in ["1", "2", "3", "4", "5", "6"]:
        produtos = {
            "1": "Pirulito",
            "2": "Doces",
            "3": "Chocolate",
            "4": "Bala",
            "5": "Frutas",
            "6": "Legumes"
        }
        produto = produtos[escolha]
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade

    elif escolha == "7":
        print("\nCarrinho de Compras:")
        print(f"{'Produto':<12} {'Qtd':<5} {'Preço Unit':<10} {'Total':<10}")
        print("-" * 40)
        total_geral = 0
        for produto, qtd in carrinho.items():
            preco = precos[produto]
            total = qtd * preco
            total_geral += total
            print(f"{produto:<12} {qtd:<5} R${preco:<10.2f} R${total:<10.2f}")
        print("-" * 40)
        print(f"{'TOTAL GERAL':<29} R${total_geral:.2f}")
