temperatura = float(input("Digite a temperatura em celsius"))
chuva = input("Esta chovendo?")
vento = input("Tem previsao de vento fortes?")

if temperatura <= 5 or temperatura >= 35:
    print("ALERTA: Temperatura Extrema!")

elif (chuva == "sim" and vento == "sim"):
    print("ALERTA: Tempestade! Evite Sair.")
elif (chuva != "sim" and temperatura > 10 and temperatura < 30):
    print ("Condiçoes ideais para atividades ao ar livre.")
