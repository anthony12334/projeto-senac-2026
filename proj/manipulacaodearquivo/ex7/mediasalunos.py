def calcular_medias_alunos():
    with open('notas.txt', 'r') as arquivo_origem, \
         open('medidas_finais.txt', 'w') as arquivo_destinado:

        for linha in arquivo_origem:
            linha = linha.strip()
            if not linha:
                continue

        partes = linha.split(',')

        if len(partes) >= 3:
            nome = partes[0]

            nota1 = float(partes[1])
            nota2 = float(partes[2])
            media = (nota1 + nota2) / 2

            arquivo_destinado.write (f"{nome}: media {media}")

            if __name__ == '__main__':

                calcular_medias_alunos()

        
        
         

