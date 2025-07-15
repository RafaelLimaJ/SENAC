import time
import Funcao
while True:

    print(f"Escolha um numero de 1 - 7\n""Par ou impar (1)\n""Calculadora(2)\n""Calculo IMC(3)\n""Tabuada(4)\n""Calculo de idade(5)\n" "Sequencia (6)\n" "Converter celsius (7)\n" "Ver Divisores Inteiros (8)\n" "Converter Kms,Ms,MMs (9)\n" "Sair(0)")

    escolha = int(input("Escolha seu numero\n"))       
          
    if escolha == 1:
        Funcao.par_impar()
    if escolha == 2:
        Funcao.calculadora()
    if escolha == 3:
        Funcao.imc()
    if escolha == 4:
        Funcao.tabuada()
    if escolha == 5:
        Funcao.calculo_idade()
    if escolha == 6:
        Funcao.sequencia()
    if escolha == 7:
        Funcao.celcius()
    if escolha == 8:
        Funcao.divisores()
    if escolha == 9:
        Funcao.km()
    if escolha == 0:
        print("Obrigado por usar nosso app")
        time.sleep(2)
        break