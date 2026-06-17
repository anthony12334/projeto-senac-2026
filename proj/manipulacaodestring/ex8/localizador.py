def buscar_palavra_no_texto(palavra_alvo):
    
    try:

        with open('documento.txt', 'r', encoding= 'utf -8') as arquivos:
            linhas = arquivos.readlines()
            
            print(f"\nBusca por '{palavra_alvo}'")
            print("-" + 30)

            encontrou = False

            for indice, conteudo in enumerate(linhas, start=1):
                if palavra_alvo.() in conteudo.
    
