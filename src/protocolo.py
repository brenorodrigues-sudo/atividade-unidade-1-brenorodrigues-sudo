class Protocolo:
    def __init__(self, numero, tipo, ano):
        self.numero = numero  
        self.tipo = tipo      
        self.ano = ano        

    def __str__(self):
        
        return f"{self.numero}-{self.tipo}-{self.ano}"

    def chave(self):
        
        return f"{self.ano}{self.tipo}{self.numero}"
