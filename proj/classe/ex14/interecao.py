class ContaBancaria:
    def __init___(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self,valor):
        self.saldo += valor

    def transferir(self, conta_destino,valor):
        if self.saldo >= valor:
            self.saldo -=valor
            conta_destino.depositar(valor)
            return True
        
        return False

