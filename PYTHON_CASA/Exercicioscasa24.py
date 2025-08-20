class Confeccao:
    def __init__(self):
        self.bolsas = []  # usar self para criar atributos da classe
        self.funcionarios = []

class Estoque:
    def __init__(self):
        self.bolsas = []  # Lista para armazenar as bolsas

    def adicionar_bolsa(self):
        nome = input("Digite o nome da bolsa para adicionar ao estoque: ")
        preco = float(input("Digite o preço da bolsa: "))
        quantidade = int(input("Digite a quantidade de bolsas: "))
        self.bolsas.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        print("Bolsa adicionada com sucesso!\n")

    def ver_bolsas(self):
        if not self.bolsas:
            print("Nenhuma bolsa no estoque.\n")
        else:
            print("\n--- ESTOQUE DE BOLSAS ---")
            for bolsa in self.bolsas:
                print(f"Nome: {bolsa['nome']} | Preço: R${bolsa['preco']} | Quantidade: {bolsa['quantidade']}")
            print()

    def menu_escolha(self):
        while True:
            print("---- MENU ----")
            print("1 - Adicionar Bolsas")
            print("2 - Ver Bolsas")
            print("3 - Sair")
            escolha = input("Digite sua escolha: ")

            if escolha == "1":
                self.adicionar_bolsa()
            elif escolha == "2":
                self.ver_bolsas()
            elif escolha == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

# Para executar:
estoque = Estoque()
estoque.menu_escolha()
