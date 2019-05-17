from DataBase.DataAccess.MySQL.MySQLDB import mySQL

class buttonModel():

    Code: int  = None
    ButtonDescription: str = None
    CodeFase: int = None

    def buscarNoBanco(self, code: int):
        
        banco = mySQL(False)
        query = f" SELECT ButtonDescription, ID, ActionDescription, CodeFase FROM Buttons INNER JOIN Actions ON CodeButton = Code WHERE Code = {code}"
        resultTuple = banco.execReadQuery(query)

        self.btnActions = list()

        for result in resultTuple:
            self.ButtonDescription = result[0]
            self.CodeFase = result[3]
            self.Code = code

    def buscarNoBancoPorFase(self, codeFase: int) -> list:
        
        listBtns = list()

        banco = mySQL(False)
        query = f" SELECT Code, ButtonDescription, ID, ActionDescription, proximaFase FROM Buttons WHERE CodeFase = {codeFase}"
        resultTuple = banco.execReadQuery(query)

        for result in resultTuple:
            btn = buttonModel()
            btn.Code = result[0]
            btn.ButtonDescription = result[1]
            btn.CodeFase = codeFase

            listBtns.append(btn)
        return listBtns

    def __init__(self):
        pass