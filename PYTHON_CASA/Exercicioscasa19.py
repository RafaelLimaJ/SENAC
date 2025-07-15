tabuada1 = int(input("Escreva o numero que deseja ver a tabuada"))
tabuada2 = int(input("Escreva ate qual numero deseja ver a tabuda"))

for tabuada2 in range (1, tabuada2+1):
    resultado = tabuada1 * tabuada2
    print (f"{tabuada1} x {tabuada2} = {resultado}")
    tabuada2 = +1