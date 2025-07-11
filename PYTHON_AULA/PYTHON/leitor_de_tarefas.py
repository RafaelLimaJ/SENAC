caminho = "tarefas.txt"

def ler_arquivo(caminho):
    with open(caminho,"r", encoding="UTF-8") as arquivo:
        print(arquivo.readlines())


with open(caminho, "a", encoding="utf-8") as arquivo:
    texto = input("Digite uma nova tarefa:\n")


    arquivo.write("\n" texto)