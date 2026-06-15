class empresa:

    def __init__(self, nome_empresa:str):
        self.nome_empresa = nome_empresa
        self.funcionarios = []

    def contratar(self, nome_funcionario):
        nome_funcionario.append(nome_funcionario)
        
        print(f"{nome_funcionario} contratado!")

    def demitir (self, nome_funcionario):
        if nome_funcionario in self.funcionarios:
            self.funcionarios.remove(nome_funcionario)