import os

# Nome da pasta principal
root_folder = "concessionaria-site"

# Subpastas e arquivos
folders = ["images"]
files = {
    "index.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>AutoPrime Concessionária</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <img src="images/logo.png" alt="Logo da Concessionária" class="logo">
        <nav>
            <ul>
                <li><a href="#">Início</a></li>
                <li><a href="#">Veículos</a></li>
                <li><a href="#">Serviços</a></li>
                <li><a href="#">Contato</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero">
        <h1>Bem-vindo à AutoPrime</h1>
        <p>Seu novo carro está aqui. Qualidade, confiança e variedade para você.</p>
    </section>

    <section class="veiculos">
        <h2>Nossos Destaques</h2>
        <div class="carros">
            <div class="carro">
                <img src="images/carro1.jpg" alt="Carro 1">
                <h3>Honda Civic 2022</h3>
                <p>Design esportivo, tecnologia avançada e conforto.</p>
            </div>
            <div class="carro">
                <img src="images/carro2.jpg" alt="Carro 2">
                <h3>Chevrolet Tracker 2023</h3>
                <p>Segurança, espaço e performance para sua família.</p>
            </div>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 AutoPrime Concessionária. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
""",
    "style.css": """body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #1a1a1a;
    color: white;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo {
    height: 50px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.hero {
    background-image: url('images/carro1.jpg');
    background-size: cover;
    background-position: center;
    padding: 100px 20px;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

.veiculos {
    padding: 40px 20px;
    text-align: center;
}

.carros {
    display: flex;
    justify-content: center;
    gap: 30px;
    flex-wrap: wrap;
}

.carro {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.carro img {
    width: 100%;
    border-radius: 8px;
}

footer {
    background-color: #1a1a1a;
    color: white;
    text-align: center;
    padding: 20px;
}
"""
}

# Criar pasta principal
os.makedirs(root_folder, exist_ok=True)

# Criar subpastas
for folder in folders:
    os.makedirs(os.path.join(root_folder, folder), exist_ok=True)

# Criar arquivos
for filename, content in files.items():
    with open(os.path.join(root_folder, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Pasta '{root_folder}' criada com sucesso com os arquivos HTML e CSS!")