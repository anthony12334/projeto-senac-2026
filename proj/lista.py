frutas = ['laranja', 'maçã', 'banana']
def primeira_fruta(frutas: list):
    return frutas[0]

animais = ['gato', 'cachorro', 'passarinho', 'coelho']
def ultimo_animal(animais: list):
    return animais[-1]

lista_de_compras = []
def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')

    return compras


if __name__ == '__main__':
    fruta = primeira_fruta(frutas)
    print(fruta)

    animais = ultimo_animal(animais)
    print(animais)
    
    compras = adicionar_compras(lista_de_compras)
    print(compras)

    

