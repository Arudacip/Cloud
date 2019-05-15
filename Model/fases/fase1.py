from abc import ABC, abstractmethod
from Model.model import model
from Model.personagem import personagem
from Model.Buttons import Buttons

class fase1(model):
    '''
        Classe que contém os dados da fase 1
    '''
    Texto: str = None
    Fase: str = None
    player: personagem = personagem()
    buttonsList: list = None

    def __init__(self, text: str, user: str):
        self.Texto = self.montaTexto(text)
        self.player.Username = user
        self.Fase = "1"
        self.buttonsList = self.montaButtons()
        super()

    def montaTexto(self, text: str) -> str:
        txt = text
        txt += '|||'
        txt += 'Você entrou no primeiro calabouço!|||A sua frente você tem 3 portas, escolha uma!'
        return txt
    
    def montaButtons(self) -> list:
        lista = list()
        lista.append(Buttons("Porta azul", "Porta azul", 0))
        lista.append(Buttons("Porta preta", "Porta preta", 0))
        lista.append(Buttons("Porta amarela", "Porta amarela", 0))
        return lista
