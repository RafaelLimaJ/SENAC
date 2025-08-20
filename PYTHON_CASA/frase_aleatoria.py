import random

# --- Listas de palavras para cada categoria ---
# Você pode adicionar ou remover palavras aqui para mudar as possibilidades
NOMES = ["CARLOS", "MARIA", "JOÃO", "ANA", "PEDRO", "SOFIA", "LUCAS"]
LOCAIS = ["A PADARIA", "O PARQUE", "A BIBLIOTECA", "O SUPERMERCADO", "A PRAIA", "A FLORESTA"]
ITENS = ["UM MAPA DO TESOURO", "UMA CHAVE DOURADA", "UM LIVRO ANTIGO", "UM GATO MISTERIOSO", "UMA POÇÃO BRILHANTE"]
ITENS2 = ["UMA CAIXA DE MADEIRA", "UMA MOCHILA VELHA", "UM BAÚ ESQUECIDO", "UMA GARRAFA DE VIDRO", "UM NINHO DE PÁSSARO"]

# --- Sorteando uma palavra de cada lista ---
nome_sorteado = random.choice(NOMES)
local_sorteado = random.choice(LOCAIS)
item_sorteado = random.choice(ITENS)
item2_sorteado = random.choice(ITENS2)

# --- Montando a frase final com as palavras sorteadas ---
frase_final = f"O {nome_sorteado} FOI ATE {local_sorteado} E ENCONTROU {item_sorteado} DENTRO DE {item2_sorteado}"

# --- Exibindo a frase gerada ---
print(frase_final)