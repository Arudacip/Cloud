from DataBase.DataAccess.MySQL.MySQLDB import mySQL

class buttonModel():

    Code: int  = None
    ButtonDescription: str = None
    CodeFase: int = None
    proximaFase: int = None

    def buscarNoBancoPorFase(self, codeFase: int) -> list:
        
        listBtns = list()

        banco = mySQL(False)
        query = f" SELECT Code, ButtonDescription, proximaFase FROM Buttons WHERE CodeFase = {codeFase}"
        resultTuple = banco.execReadQuery(query)

        for result in resultTuple:
            btn = buttonModel()
            btn.Code = result[0]
            btn.ButtonDescription = result[1]
            btn.proximaFase = result[2]
            btn.CodeFase = codeFase

            listBtns.append(btn)
        return listBtns

    def __init__(self):
        pass