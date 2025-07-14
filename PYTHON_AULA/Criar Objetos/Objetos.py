class Moto:
    def __init__(self,cor,ano,modelo):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo


    def Dar_re():
        print("Pii-pii")
    
    def Buzinar():
        print("BI-BI")
    
    def Acelerar():
        print("Vrum-Vrum")
    
    def get_info(self):
        return f"Cor: {self.cor} \nAno: {self.ano} \nModelo: {self.modelo}"

moto1 = Moto("Azul",2023,"moto") 