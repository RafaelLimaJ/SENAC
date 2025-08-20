import requests

# 🔑 COLOQUE SUA NOVA API KEY AQUI
api_key = "RGAPI-d365de56-8157-46a6-9f74-695975e44963"

# 🎯 Match ID da partida
match_id = "df604098-01de-425e-9902-8e4183c13c77"

# 🌍 Endpoint correto para Valorant (sempre 'americas')
url = f"https://americas.api.riotgames.com/val/matches/{match_id}"

# 🔒 Cabeçalho com sua API Key
headers = {"X-Riot-Token": api_key}

print("🔄 Consultando a API da Riot...")

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("✅ Dados da partida encontrados com sucesso!\n")
        print(response.json())  # Exibe o JSON completo com as estatísticas da partida
    elif response.status_code == 401:
        print("❌ Erro 401: Não autorizado. Verifique sua API Key.")
    elif response.status_code == 403:
        print("❌ Erro 403: Acesso proibido. Sua API Key está inválida ou expirada.")
    elif response.status_code == 404:
        print("❌ Erro 404: Partida não encontrada. Verifique se o Match ID está correto.")
    else:
        print(f"⚠️ Erro {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print("⚠️ Erro ao conectar na API:", e)
