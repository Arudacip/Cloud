from abc import ABC, abstractmethod
from Model.Buttons import Buttons
from Model.personagem import personagem
from Model.fases.DB_Models.faseLigacao import faseLigacao

class faseModel(ABC):

    @property
    @abstractmethod
    def FaseLigacao() -> lista:
        '''
            Lista de ligações que a fase realiza
        '''
        pass

    @property
    @abstractmethod
    def classNameFaseImplementation() -> str:
        '''
            Nome da classe da fase
        '''
        pass

    @property
    @abstractmethod    
    def Code() -> int:
        '''
            Codigo único da fase
        '''
        pass

    @property
    @abstractmethod
    def CorFase() -> str:
        '''
            Cor da fase, seguindo principios do atributo COLOR do arborJS
        '''
        pass

    @property
    @abstractmethod
    def LabelFase() -> str:
        '''
            Label da fase, nome curto
        '''
        pass

    @property
    @abstractmethod
    def NomeFase() -> str:
        '''
            Nome da fase
        '''
        pass

    @property
    @abstractmethod 
    def ShapeFase() -> str:
        '''
            Shape da fase que deverá ser feito no grafo
        '''
        pass

    def __init__(self):
        pass