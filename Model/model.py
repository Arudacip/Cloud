from abc import ABC, abstractmethod

class model(ABC):
    
    @property
    @abstractmethod
    def Text(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def Username(self):
        raise NotImplementedError

    def __init__(self):
        pass