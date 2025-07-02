nota1 = int(input("Primeira nota"))
nota2 = int(input("Segunda nota"))
nota3 = int(input("Terceira nota"))
nota4 = int(input("Quarta nota"))

conta = (nota1 + nota2 + nota3 + nota4) / 4

if conta >= 6:
    print(f"Media = {conta}")
    print("Aprovado")
else:
    print(f"Media = {conta}")
    print ("Reprovado")