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
    
    def add_professor(self):
        nome = input("Digite o nome")
        idade =  int(input("Digite a idade"))
        id = int(input("Digite o ID"))

        novo_professor = Professores(nome,idade,id)
        self.professores.append(novo_professor)
        print("Professor cadastrado")

    def listar_professores(self):
        print("\n--- Professores Cadastrados ---")
        for professor in self.professores:
            print(f"Nome:{professor.nome} Idade:{professor.idade} Id:{professor.id}")


    def listar_alunos(self):
        print("\n--- Alunos Cadastrados ---")
        for aluno in self.alunos:
            print(f"Nome:{aluno.nome} Idade:{aluno.idade} Id:{aluno.id}")

class Pessoa:

    def __init__(self,idade,nome,id):
        self.idade = idade
        self.nome = nome
        self.id = id
    def salario():
        print("Possui salario")
        

        

class Alunos(Pessoa):
    def __init__(self,idade,nome,id):
        super().__init__(idade,nome,id)
    def salario():
            print("Nao possui salario")

class Professores(Pessoa):
    def __init__(self,idade,nome,id):
        super().__init__(idade,nome,id)
        self.materia = "português"

escola = Escola()    
while True:
    print("1 - Lista de alunos\n2 - Adicionar aluno\n3 - Lista de professores\n4 - Adicionar professores")
    escolha = int(input("Digite sua escolha"))
    if escolha == 1:
        escola.listar_alunos()
    if escolha == 2:
        escola.add_aluno()
    if escolha == 3:
        escola.listar_professores()
    if escolha == 4:
        escola.add_professor()


    



 
