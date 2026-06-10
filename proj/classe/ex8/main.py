from playlist import Playlist

if __name__ == '__main__':

    Playlist = playlist('rock')
    playlist.adcionar_musica('come as you are')
    assert len(playlist.musicas) == 1

    assert playlist.remover_musica('drain you') \
         == 'musica não encontrada'
    
    playlist.remover_musica('come as you are')

    assert len(playlist.musicas) ==0