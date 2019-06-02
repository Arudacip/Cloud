from DataBase.DataAccess.MySQL.MySQLDB import mySQL

from Model.DB_Models.faseModel import faseModel

class faseGraph():

    def buscarNoBanco(self, codeFaseAtual: int) -> list:

        banco = mySQL(False)

        ligacoes = list()

        query = f" SELECT ID, CodeProximaFase FROM FaseLigacoes WHERE CodeFaseAtual = {codeFaseAtual}"

        resultTuple = banco.execReadQuery(query)

        for result in resultTuple:
            ligacoes.append(result[0], result[1], codeFaseAtual)

        return ligacoes

    def __init__(self):
        pass

class data():
    nodes: list = None #Lista de faseNode
    edges: list = None #Lista de nodes

    def generateNodes(self):
        Models = faseModel()
        listaDeModels = Models.buscarTodos()
        self.nodes = faseNode.importFromFaseModelList(listaDeModels)

    def generateEdges(self):
        pass

class faseNode():

    color: str = None
    shape: str = None
    label: str = None

    @staticmethod
    def importFromFaseModelList(listaDeFaseModels: list) -> list:

        listaDeFaseNode: list = None

        for faseModel in listaDeFaseModels:
            listaDeFaseNode.append(faseNode.importFromFaseModel(faseModel))

        return listaDeFaseNode
    
    @staticmethod
    def importFromFaseModel(FaseModel: faseModel) -> faseNode:
        node = faseNode()
        node.color = faseModel.CorFase
        node.label = faseModel.LabelFase
        node.shape = faseModel.ShapeFase
        return node
