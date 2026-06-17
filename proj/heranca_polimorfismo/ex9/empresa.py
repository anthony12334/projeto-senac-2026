class Funcionario:
    def trabalhar(self):
        return 'realizando tarefas basicas'

class Gerente:
    def trabalhar(self):
        return super(). trabalhar() + ' e revisando relatório'   