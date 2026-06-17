class Heroi:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def atacar(self):
        return "não há arma disponível!"
    
class Mago(Heroi):
    def __init__(self, nome, vida, poder_magico):
        super().__init__(nome,vida)
        self.poder_magico = poder_magico
    def atacar(self):
        dano = self.poder_magico = poder_magico
        return f"{self.nome} atacou com magia! Dano: {dano}"

class Guerreiro(Heroi):
    def __init__ (self, nome, vida, forca_fisica):
        super().__init__(self, nome, vida)
        self.forca_fisica

    def atacar(self):
        dano = self.forca_fisica * 2
        return f"{self.nome} atacou com força bruta! Dano {dano}"
        
    