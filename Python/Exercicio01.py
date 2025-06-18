Nome = input ("Qual é o seu nome?")
idade = int(input("Quantos anos você tem?"))
IDADE_MINIMA = 16
BATATA = ("Voce tem autorizaçao")
if idade > IDADE_MINIMA:
    print("Bem vindo") 
else:
    permissao = input("Você tem autorizaçao dos seus pais? Sim/Não")
    if permissao == "Sim":    
        print ("Bem vindo")
    else:
        print ("acesso Negado")

