from Model.DB_Models.Personagem import personagem
from Model.DB_Models.faseLigacao import faseLigacao
from Model.DB_Models.buttonModel import buttonModel

from DataBase.DataAccess.MySQL.MySQLDB import mySQL

from jsonConverter import convertToJson

from json import dumps

class faseModel():

    btnsList: list = None
    
    FaseLigacao: list = None

    Texto: str = None

    Code:int = None

    CorFase: str = None

    LabelFase: str = None

    NomeFase: str = None

    ShapeFase: str = None

    '''def inserirNoBanco(self):
        banco = mySQL(False)

        query = " INSERT INTO Fases (Code, CorFase, ShapeFase, NomeFase, LabelFase, classNameFaseImplementation) VALUES "
        query += f" ( {self.Code}, '{self.CorFase}', '{self.ShapeFase}', '{self.NomeFase}', '{self.LabelFase}', '{self.classNameFaseImplementation}' )"

        banco.execModQuery(query)

        queryLigacoes = "INSERT INTO FaseLigacoes (CodeFaseAtual, CodeProximaFase) VALUES "

        for ligacao in self.FaseLigacao:
                queryLigacoes += f" ( '{ligacao.CodeFaseAtual}', '{ligacao.CodeProximaFase}'  ) "'''

    def buscarTodos(self) -> list:
        fases = list()
        banco = mySQL(False)
        query = f" SELECT CorFase, ShapeFase, NomeFase, LabelFase, texto, Code FROM Fases"
        resultTuple = banco.execReadQuery(query)
        for result in resultTuple:
            fase = faseModel()
            fase.CorFase = result[0]
            fase.ShapeFase = result[1]
            fase.NomeFase = result[2]
            fase.LabelFase = result[3]
            fase.Texto = result[4]
            fase.Code = result[5]
            fases.append(fase)
        return fases

    def buscarNoBanco(self, code: int):
        try:
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

            self.btnsList = buttonModel().buscarNoBancoPorFase(code)
        except Exception:
            self.Code = -1
        

    def __init__(self):
        pass

    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def convertFasesToJson() -> str:
    fases = faseModel().buscarTodos()

    return dumps([ fse.__dict__ for fse in fases ])

def convertFasesToArborJSData() -> str:
    pass

class graphDataFase():
    nodes: list = None
    edges: list = None