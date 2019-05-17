from DataBase.DataAccess.MySQL.MySQLDB import mySQL

class faseLigacao():

    CodeFaseAtual: int = None
    CodeProximaFase: int = None
    _ID: int = None 

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

    def __init__(self, ID: int, CodeFaseAtual: int, CodeProximaFase: int):
        self.CodeFaseAtual = CodeFaseAtual
        self.CodeProximaFase = CodeProximaFase
        self._ID = ID
        pass