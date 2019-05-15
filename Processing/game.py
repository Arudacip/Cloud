from flask import request

from Model.texto import texto
from Model.model import model
from Model.personagem import personagem
from Model.Buttons import Buttons
from Model.fases.faseController import faseControler

class game():
    faseCtrl: faseControler = None
    def __init__(self):
        self.faseCtrl = faseControler()
    
    def firstPost(self) -> model:
        resposta = request.form.get('user')
        txt = request.form.get('texto')
        txt = txt.strip('Bem vindo ao jogo! Para darmos inicio, digite seu nome.')
        Modelo = texto( txt , resposta, '0')
        return Modelo

    def notFirstPost(self) -> model:
        Modelo = None
        fase = request.form.get('fase')
        if(fase == '0'): #da fase 0 para a fase 1
            Modelo = self.faseCtrl.criarFase1(request.form.get('texto'), request.form.get('user'))
        return Modelo 