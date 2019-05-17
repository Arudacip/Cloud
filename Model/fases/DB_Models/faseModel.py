from Model.personagem import personagem
from Model.fases.DB_Models.faseLigacao import faseLigacao
from Model.fases.DB_Models.buttonModel import buttonModel

from DataBase.DataAccess.MySQL.MySQLDB import mySQL

class faseModel():

    btnsList: list = None
    
    FaseLigacao: list = None

    Texto: str = None

    Code:int = None

    CorFase: str = None

    LabelFase: str = None

    NomeFase: str = None

    ShapeFase: str = None

    def inserirNoBanco(self):
        banco = mySQL(False)

        query = " INSERT INTO Fases (Code, CorFase, ShapeFase, NomeFase, LabelFase, classNameFaseImplementation) VALUES "
        query += f" ( {self.Code}, '{self.CorFase}', '{self.ShapeFase}', '{self.NomeFase}', '{self.LabelFase}', '{self.classNameFaseImplementation}' )"

        banco.execModQuery(query)

        queryLigacoes = "INSERT INTO FaseLigacoes (CodeFaseAtual, CodeProximaFase) VALUES "

        for ligacao in self.FaseLigacao:
                queryLigacoes += f" ( '{ligacao.CodeFaseAtual}', '{ligacao.CodeProximaFase}'  ) "

    def buscarNoBanco(self, code: int):
        banco = mySQL(False)
        query = f" SELECT CorFase, ShapeFase, NomeFase, LabelFase, texto FROM Fases WHERE Code = {code}"
        resultTuple = banco.execReadQuery(query)
        for result in resultTuple:
            self.CorFase = result[0]
            self.ShapeFase = result[1]
            self.NomeFase = result[2]
            self.LabelFase = result[3]
            self.Texto = result[4]
            self.Code = code

        self.FaseLigacao = faseLigacao(0,0,0).buscarNoBanco(code)
        self.btnsList = buttonModel().buscarNoBancoPorFase(code)
        

    def __init__(self):
        pass