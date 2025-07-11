altura = float(input("Qual sua altura"))
peso = float(input("Qual seu peso?"))
Imc = peso / (altura * altura)
if Imc > 25:
    print(f"Voce esta acima do peso seu IMC é {Imc}")
else:
    print(f"Seu peso esta OK seu IMC é {Imc}")