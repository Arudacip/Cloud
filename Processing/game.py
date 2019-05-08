from flask import request

from Model.texto import texto
from Model.model import model

class game():
    def __init__(self):
        pass
    
    def firstPost(self) -> model:
        resposta = request.form.get('user')
        txt = request.form.get('texto')
        txt = txt.strip('Bem vindo ao jogo! Para darmos inicio, digite seu nome.')
        txt += 'Bem vindo: ' + resposta + '. O jogo começou!'
        Modelo = texto( txt , resposta)
        return Modelo

    def notFirstPost(self) -> model:
        return texto( 'oi', 'tchau') 