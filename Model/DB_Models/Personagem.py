from Model.fases.DB_Models.faseLigacao import faseLigacao
from Model.fases.DB_Models.buttonModel import buttonModel

from DataBase.DataAccess.MySQL.MySQLDB import mySQL

from jsonConverter import convertToJson

from json import dumps

import datetime

class personagem():

    ID: int = None
    NomeJogador: str = None
    StartGameTime: str = None

    def inserirNoBancoStartGame(self) -> int:
        banco = mySQL(False)
        time = datetime.datetime.now()
        query = " INSERT INTO StartGame (NomeJogador, StartGameTime) VALUES "
        query += f" ( {self.NomeJogador}, '{time}' )"

        banco.execModQuery(query)

        query = f"SELECT ID FROM StartGame WHERE NomeJogador = '{self.NomeJogador}' AND StartGameTime = '{time}'"
        resultTuple = banco.execReadQuery(query)
        for result in resultTuple:
            self.ID = result[0]

    def inserirNoBancoCaminhoJogo(self):
        raise NotImplementedError
    def inserirNoBancoEndGame(self):
        raise NotImplementedError

    def buscarNoBanco(self, ID: int):
        banco = mySQL(False)
        query = f" SELECT NomeJogador, StartGameTime FROM Fases WHERE ID = {ID}"
        resultTuple = banco.execReadQuery(query)
        for result in resultTuple:
            self.NomeJogador = result[0]
            self.StartGameTime = result[1]
            self.ID = ID

    def __init__(self):
        pass

    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)