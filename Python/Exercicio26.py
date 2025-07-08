lista = []
while True:
    tarefas = input("Adicione novas tarefas")
    lista.append(tarefas)
    print(lista)
    if tarefas == "remover":
        print("DIGITE OQUE VOCE QUER REMOVER")
        deletar = input()
        lista.remove(deletar)
        lista.remove("remover")
        print(lista)

