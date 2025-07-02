import pyfiglet

frase = input("Digite uma frase.")

frase_ascii = pyfiglet.figlet_format(frase)
print (frase_ascii)