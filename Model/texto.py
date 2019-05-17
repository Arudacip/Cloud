
from Model.personagem import personagem

class texto():
    '''
        Classe que contém um texto simples
    '''
    Texto: str = None
    Fase: str = None
    player: personagem = None
    buttonsList: list = None

    def __init__(self, text: str, user: str, fase: int):

        self.btnsList = list()
        self.player = personagem()
        self.player.Username = user

        self.Texto = text
        self.Fase = fase

        super()
        pass