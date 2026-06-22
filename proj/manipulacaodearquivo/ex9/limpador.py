def limpar_arquivos(origem, destino):
    try:
        linhas_limpas = []

        with open(origem, 'r', encoding= 'uft-8') as arquivo:
            for linha in arquivo:

                if linha.strip():
                    linhas_limpas.append(linha)

        with open(destino, 'w', encoding= 'uft-8') as arquivo_final:
            arquivo_final.writelines(linhas_limpas)

        print(f"arquivo limpo salvo em: {destino}")

    except FileNotFoundError:
        print("erro: o arquivo de origem não foi encontrado")

    except Exception as e:
        print("ocorreu um erro inesperado")            

                   
          