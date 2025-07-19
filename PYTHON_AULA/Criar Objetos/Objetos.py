class Escola:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.salas = []
    
    def add_aluno(self):
        nome = input("Digite o nome")
        idade =  int(input("Digite a idade"))
        id = int(input("Digite o ID"))

        novo_aluno = Alunos(nome,idade,id)
        self.alunos.append(novo_aluno)
        print("Aluno cadastrado")
    
    def listar_alunos(self):
        print("\n--- Alunos Cadastrados ---")
        for aluno in self.alunos:
            print(f"Nome:{aluno.nome} Idade:{aluno.idade} Id:{aluno.id}")


class Alunos:

    def __init__(self,idade,nome,id):
        self.idade = idade
        self.nome = nome
        self.id = id

escola = Escola()    
while True:
    print("1 - Lista de alunos\n2 - Adicionar aluno")
    escolha = int(input("Digite sua escolha"))
    if escolha == 1:
        escola.listar_alunos()
    if escolha ==2:
        escola.add_aluno()


    



 
