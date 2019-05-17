from DataBase.DataAccess.MySQL.MySQLDB import mySQL

class buttonModel():

    Code: int  = None
    ButtonDescription: str = None
    btnActions: list = list()
    CodeFase: int = None

    def buscarNoBanco(self, code: int):
        
        banco = mySQL(False)
        query = f" SELECT ButtonDescription, ID, ActionDescription, CodeFase FROM Buttons INNER JOIN Actions ON CodeButton = Code WHERE Code = {code}"
        resultTuple = banco.execReadQuery(query)

        self.btnActions = list()

        for result in resultTuple:
            self.ButtonDescription = result[0]
            self.btnActions.append(buttonActions(result[1], result[2], code))
            self.CodeFase = result[3]
            self.Code = code

    def buscarNoBancoPorFase(self, codeFase: int) -> list:
        
        listBtns = list()

        banco = mySQL(False)
        query = f" SELECT Code, ButtonDescription, ID, ActionDescription FROM Buttons INNER JOIN Actions ON CodeButton = Code WHERE CodeFase = {codeFase}"
        resultTuple = banco.execReadQuery(query)

        for result in resultTuple:
            btn = buttonModel()
            btn.Code = result[0]
            btn.ButtonDescription = result[0]
            btn.btnActions.append(buttonActions(result[1], result[2], result[0]))
            btn.CodeFase = codeFase

            listBtns.append(btn)
        return listBtns

    def __init__(self):
        pass

class buttonActions():

    ID: int = None
    ActionDescription: str = None
    CodeButton: int = None

    def __init__(self, ID: int, ActionDescription: str, CodeButton: int):
        pass