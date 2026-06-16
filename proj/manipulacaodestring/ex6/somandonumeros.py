def somar_valores_arquivos():
    total = 0.0
    with open('valores.txt', 'r')as aquivos:
        for linha in arquivo:

            numero = float(linha.strip())

            print(f"o somatorio total é: {total}")
