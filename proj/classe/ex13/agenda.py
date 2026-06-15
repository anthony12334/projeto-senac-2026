class agenda:

    def __init__(self):
                
        self.nomes = []
        
        self.telefones = []
    def salvar_contatos(self, nome, telefone):
        self.nomes.append(nome)
        self.telefones.append(telefone)

    def buscar_telefone(self, nome_pesquisado):
        if nome_pesquisado in self.nomes:
            indice = self.nomes.index(nome_pesquisado)
            return self.telefones[indice]
        else:
            return "contato não encontrado"
