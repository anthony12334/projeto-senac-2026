def fazer_backup_dados(nome_arquivo_original):
    try:

        nome_arquivo_backup = nome_arquivo_original + ".bak"
        
        with open(nome_arquivo_original, 'r' encoding= 'uft-8'):
        conteudo = original.read()

        with open(nome_arquivo_backup, 'w', encoding= 'uft-8') as backup:
            backup.write(conteudo)

        print(f"backup concluido com sucesso: {n}")