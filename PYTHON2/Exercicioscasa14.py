print("PEDRA PAPEL OU TESOURA")
print(" -PEDRA   (1) \n -PAPEL   (2) \n -TESOURA (3)")
resposta = int(input("ESCOLHA O NUMERO DE QUAL VOCE QUER JOGAR"))
resposta2 = int(input("ESCOLHA O NUMERO DE QUAL VOCE QUER JOGAR"))


if resposta == 1 and resposta2 == 3:
    print ("PEDRA GANHOU!!")  
if resposta == 1 and resposta2 == 2:
    print ("PAPEL GANHOU!!")  
if resposta == 2 and resposta2 == 1:
    print ("PAPEL GANHOU!!")
if resposta == 2 and resposta2 == 3:
    print ("TESOURA GANHOU!!")  
if resposta == 3 and resposta2 == 1:
    print ("PEDRA GANHOU!!")  
if resposta == 3 and resposta2 == 2:
    print ("TESOURA GANHOU!!") 