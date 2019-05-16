from abc import ABC, abstractmethod
from Model.Buttons import Buttons
from Model.personagem import personagem
from Model.fases.DB_Models.faseModel import faseModel

class model(ABC):
    
    buttonsList: list = None
    player: personagem = None

    @property
    @abstractmethod
    def Texto(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def Fase(self) -> faseModel:
        raise NotImplementedError

    def __init__(self):
        pass