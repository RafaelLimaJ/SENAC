
class pessoa:
    def __init__(self,nome,idade,altura):
        self.altura = altura
        self.idade = idade
        self.nome = nome
    
    def calculo_idade(self):
        if self.idade >= 18:
            return "Maior de idade"
        else:
            return "Menor de idade"
while True:    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = int(input("Digite sua altura (em cm): "))


pessoa = pessoa(nome, idade, altura)

print(f"{pessoa.nome} tem {pessoa.idade} anos, altura de {pessoa.altura}cm e é {pessoa.calculo_idade()}.")
