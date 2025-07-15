idade = int(input("IDADE?"))



menu_adulto = ["Bem vindos a Nossa Concessionária!", "Aqui abaixo Nossos Modelos", "-BMW: A partir de R$300.000", "-Toyota: A partir de R$100.000", "-Mercedes-benz: A partir de R$350.000", "-Honda: A partir de R$120.000", "-Ford: A partir de R$90.000"]

menu_criança = ["Sugestao de carrinhos e Filmes!!! ", "-Hot Wheels (a coleçao Toda!", "-Filme Carros (Relampago MCQUEEN KTCHAUU!", "-Blaze and Monster Machines", "-Patrulha canina (com seus veiculos de resgate!)", "-Thomas e seus Amigos!"]
if idade < 18:
    for I in menu_criança:
        print(I)

else:
    for f in menu_adulto:
        print(f)