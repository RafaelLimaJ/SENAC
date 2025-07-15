agenda = []

while True:
    print("---- MENU ----")
    print("1 - Adicionar Nome/Telefone")
    print("2 - Procurar Nome/Telefone")
    print("3 - Sair")

    escolha = input("Digite o número da escolha (1 - 3): ")

    if escolha == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        contato = {
            "nome": nome,
            "telefone": telefone
        }
        agenda.append(contato)
        print("Contato adicionado com sucesso.\n")

    elif escolha == "2":
        encontrar = input("Digite o nome da pessoa que deseja procurar: ")
        encontrado = False
        for pessoa in agenda:
            if pessoa["nome"].lower() == encontrar.lower():
                print(f"Pessoa encontrada:\nNome: {pessoa['nome']} / Telefone: {pessoa['telefone']}\n")
                encontrado = True
                break
        
        if not encontrado:
            add_pessoa = input("Pessoa não encontrada. Deseja adicionar? (sim/não): ").strip().lower()
            if add_pessoa == "sim":
                telefone = input("Digite o telefone da pessoa: ")
                novo_contato = {
                    "nome": encontrar,
                    "telefone": telefone
                }
                agenda.append(novo_contato)
                print("Pessoa adicionada com sucesso.\n")
            else:
                print("Ok, obrigado por usar nossa agenda.\n")

    elif escolha == "3":
        print("Saindo da agenda. Até logo!")
        break

    else:
        print("Escolha inválida. Digite uma opção entre 1 e 3.\n")
