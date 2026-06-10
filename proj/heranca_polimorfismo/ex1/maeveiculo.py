class veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class carro(veiculo):
    pass

meu_carro = carro("gtrr35", 2024)
print(meu_carro.marca)