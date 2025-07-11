import os
tarefas = "tarefas.txt"
with open(tarefas,"a", encoding="utf-8") as arquivo:
    arquivo.write("")
    
def Ver_tarefas(tarefas):
        with open(tarefas, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read()
            print(linhas)
def add_tarefas(tarefas):
      
    add = input("Digite oque deseja adicionar na lista")
    with open(tarefas, "a", encoding="utf-8") as arquivo:
        arquivo.write(add + "\n")

while True:
    print("1 - Adicionar Tarefas\n2 - Ver Tarefas\n3 - Sair")


    try:
        escolha = int(input("Escolha uma opçao\n"))
        if escolha == 1:
            add_tarefas(tarefas)
        if escolha == 2:
            Ver_tarefas(tarefas)
        if escolha == 3:
            break
    except ValueError:
        print("Valor invalido digite apenas numeros")
