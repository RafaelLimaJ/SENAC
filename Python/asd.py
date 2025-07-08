agenda = []

while True:
    contato = {
        "nome": "",
        "telefone": ""
    }
    
    print("\n--- MENU ---")
    print("1. Adicionar contato")
    print("2. Procurar contato")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1/2/3): ")
    
    if opcao == "1":
        # Adicionar novo contato
        contato["nome"] = input("Digite o nome: ")
        contato["telefone"] = input("Digite o telefone: ")
        agenda.append(contato.copy())  # Usamos .copy() para evitar sobrescrita
        print("\nContato adicionado com sucesso!")
        
    elif opcao == "2":
        # Procurar contato
        nome_procurado = input("\nDigite o nome para procurar: ")
        encontrado = False
        
        for pessoa in agenda:
            if pessoa["nome"].lower() == nome_procurado.lower():  # Comparação sem case-sensitive
                print(f"\nContato encontrado: {pessoa['nome']} - {pessoa['telefone']}")
                
                encontrado = True
                break
        
        if not encontrado:
            print("\nContato não encontrado na agenda.")
    
    elif opcao == "3":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")