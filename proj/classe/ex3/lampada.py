class Lampada:

    ligada: bool

    def __init__(self):
        self.ligada = False

    def clicar_interrruptor(self):
        if not self.ligada:
            self.ligada = True
        else:
            self.ligada = False
        
    def status(self):
        if self.ligada:
            return "A lâmpada esta ligada"
        return "A lâmpada esta desligada"
        