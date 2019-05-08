from abc import ABC, abstractmethod
from Model.model import model

class texto(model):
    Text = None
    Username = None
    def __init__(self, text: str, user: str):
        self.Text = text
        self.Username = user
        super()
        pass