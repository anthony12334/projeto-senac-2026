def __init__(self, nome. idade):
    self.idade = idade 
    self.nome = nome

if __name__ == '__main__':

    while(true):

        print("1 - criar pessoa: ")
        print("2 - mostar pessoas: ")
        print("3 - sair! ")

        escolha = int(input("\N escolha uma opção: "))

       if escolha == 1:
        nome = input("digite o nome da pessoa: ")
        idade = input("digite a idade da pessoa: ")


