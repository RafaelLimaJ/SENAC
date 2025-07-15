idade = int(input("Escreva sua idade"))
clube = input("Você participa do clube?")

if (idade >= 60 and clube == "sim"):
    print("Ok, você ganhou um desconto VIP")

elif (idade >=60 or clube == "sim"):
    print("Ok, você ganhou um desconto basico")

else:
    print("Sem desconto disponivel.")