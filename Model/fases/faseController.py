from Model.fases.DB_Models.faseModel import faseModel
from Model.model import model

class faseControler():

    def criarFase1(self, texto: str, user: str) -> model:
        fase = faseModel()
        fase.buscarNoBanco(0)  
        fase.Texto = texto + "|||" + fase.Texto

        mdl = model()
        
        mdl.Fase = fase
        mdl.player = None
        return mdl
