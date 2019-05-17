from flask import request

from Model.texto import texto
from Model.model import model
from Model.personagem import personagem
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
        if(fase == '-1'): #da fase -1 para a fase 0 (Inicio de jogo)
            Modelo = self.faseCtrl.criarFase1(request.form.get('texto'), request.form.get('user'))
        return Modelo 