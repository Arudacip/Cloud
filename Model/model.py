from abc import ABC, abstractmethod

class model(ABC):
    
    @property
    @abstractmethod
    def Text(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def Username(self) -> str:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def BtnQtd(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def BtnDescrptions(self) -> list:
        raise NotImplementedError

    def __init__(self):
        pass