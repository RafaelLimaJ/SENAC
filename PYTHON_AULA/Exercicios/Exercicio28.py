agenda = []

while True:
    contatos = {
        "nome": "",
        "telefone": ""
    }
    print("----MENU----")
    print("1- Adicionar Nome/telefone")
    print("2- Procurar Nomes/telefones")
    print("3- Sair.")

    escolha = input("Digite o numero da escolha (1 - 3)")
    
    if escolha == "1":
        
        adicionar_nome = input("Digite o nome")
        adicionar_telefone = input("Digite o telefone")
        
        contatos["nome"] = adicionar_nome
        contatos["telefone"] = adicionar_telefone
        agenda.append(contatos)

    if escolha == "2":
        encontrar = input("Digite o nome da pessoa que deseja procurar.: ")
        for pessoa in agenda:
            if pessoa["nome"] == encontrar:
                print(f"Pessoa encontrada. \n{pessoa['nome']} / {pessoa['telefone']}")
