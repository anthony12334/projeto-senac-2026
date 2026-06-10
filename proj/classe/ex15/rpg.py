class personagem:
    def __init__(self, nome, vida,ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def vivo(self):
        return self.vida > 0

    def receber_dano(sellf, quantidade):
        self.vida -= quantidade
        self.vida < 0
        self.vida = 0

    def atacar(self,oponente):
        if self.vivo():
            oponente.receber_dano(self.ataque)