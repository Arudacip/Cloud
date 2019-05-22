from Model.DB_Models.faseModel import faseModel
from Model.DB_Models.Personagem import personagem

from Model.model import model


class faseControler():

    def criarFaseN1(self, texto: str, user: str) -> model:
        fase = faseModel()
        fase.buscarNoBanco(0)
        fase.Texto = texto + "|||" + fase.Texto

        mdl = model()
        
        mdl.Fase = fase
        mdl.player = personagem()
        
        return mdl

    def criarFaseN2(self, texto:str, user: str, nxtFase: str) -> model:
        txt = texto or "Bem vindo ao jogo! Para darmos inicio, digite seu nome."
        fase = faseModel()
        fase.buscarNoBanco(nxtFase)
        fase.Texto = txt + "|||" + fase.Texto

        mdl = model()

        mdl.Fase = fase
        mdl.player = None
        return mdl