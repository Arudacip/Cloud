from abc import ABC, abstractmethod
from Model.Buttons import Buttons
from Model.personagem import personagem

class model(ABC):
    
    buttonsList: list = None
    player: personagem = None

    @property
    @abstractmethod
    def Texto(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def Fase(self) -> int:
        raise NotImplementedError

    def __init__(self):
        pass