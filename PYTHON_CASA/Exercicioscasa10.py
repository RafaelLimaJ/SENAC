Nota1 = int(input("Digite a primeira nota"))
Nota2 = int(input("Digite a segunda nota"))
Nota3 = int(input("Digite a terceira nota"))
Nota4 = int(input("Digite a quarta nota"))

calculo = (Nota1 + Nota2 + Nota3 + Nota4) / 4

if calculo > 6:
    print(f"O aluno esta aprovado a media dele foi {calculo}")
else:
    print (f"O aluno foi reprovado a media dele foi {calculo}")