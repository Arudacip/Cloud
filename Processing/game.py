from flask import request

from Model.texto import texto
from Model.model import model
from Model.DB_Models.Personagem import personagem
from Processing.faseController import faseControler

class game():
    faseCtrl: faseControler = None
    def __init__(self):
        self.faseCtrl = faseControler()
    
    def firstPost(self) -> model:
        resposta = ""#request.form.get('user')
        txt = ""
        txt = txt.strip('Bem vindo ao jogo! Para darmos inicio, digite seu nome.')
        Modelo = texto( txt , resposta, '-1')
        return Modelo

    def notFirstPost(self) -> model:
        Modelo = None
        fase = request.form.get('fase')
        nxtFase = request.form.get('nextFase')
        if(fase == '-1'): #da fase -1 para a fase 0 (Inicio de jogo)
            Modelo = self.faseCtrl.criarFaseN1(request.form.get('texto'), request.form.get('user'))
        if(fase == '0'):
            Modelo = self.faseCtrl.criarFaseN2(request.form.get('texto'), request.form.get('user'), nxtFase)
        return Modelo 

    def nextFase(self, nxtFase:str ) -> model:
        Modelo: model = self.faseCtrl.criarFaseN2(request.form.get('texto'), request.form.get('user'), nxtFase)
        if int(Modelo.Fase.Code) < 0:
            return None
        return Modelo 