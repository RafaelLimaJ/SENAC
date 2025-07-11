while True:
    nota1 = int(input("NOTA 1\n"))
    nota2 = int(input("NOTA 2\n"))
    media = (nota1 + nota2) / 2
    if media < 4:
        print ("aluno reprovado")
    if media >= 7:
        print ("aluno aprovado")
    if 7 > media > 4:
        recuperaçao = int(input("Qual sua nota de recuperaçao?"))
        media2 = (nota1 + nota2 + recuperaçao) / 3
        if media2 >= 5:
            print (f"Voce esta Aprovado sua media com a recuperaçao foi {media2}")
        else:
            print (f"Voce esta Reprovado sua media com a recuperaçao foi {media2}")

