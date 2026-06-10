class Playlist:

    nome:str

    def __init__(self, nome:str):
        self.nome = nome
        self.musicas = []

    def remover_musica(self, nome_musica:str):
        if nome_musica in self.musica:
            self.musicas.remove(nome_musica)
        else:

            

  
