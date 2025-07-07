import random
limite = int(input("Quantas faces o dado tera?"))
def lançar_dados(dado):
    print (f"O dado caiu na face {dado} de {limite}")

dado = random.randint(1,limite)

lançar_dados(dado)