escolha = int(input("Digite sua escolha."))
class Concessionaria:
    def __init__(self):
        self.cor = []
        self.ano = []
        self.modelo = []    
        self.quantidades = []
    def add_motos():
        id = int(input("Digite o ID"))
        ano = int(input("Digite o ano da moto"))
        cor = input("Digite a cor")
        modelo = input("Digite o modelo")
        quantidade = int(input("Digite a quantidade de motos"))
        motos = (id,ano,cor,modelo,quantidade)
        
        return motos
    def menu_da_concessionaria():
        menu = ["Ver modelos","Adicionar modelos"]
        for i,alternativa in enumerate(menu):
            print(f"{i+1} {alternativa}")
    
    def escolha_do_usuario(add_motos,escolha):
            if escolha == 1:
                print(1)
            elif escolha == 2:
                add_motos()

    def adicionar_motos_na_lista(add_motos):
         pass


