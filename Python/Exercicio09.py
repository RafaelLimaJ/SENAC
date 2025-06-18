#Esse é meu primeiro dicionario
eletrodomesticos = {
    "tipo":"tv",
    "marca":"samsung",
    "polegadas":80
}

Estante = {
    "eletrodomestico1" : eletrodomesticos,
    "eletrodomestico2" : {
        "tipo": "microondas",
        "marca": "eletrolux",
        "potencia": "1000w"
        }
}
print(eletrodomesticos.values())