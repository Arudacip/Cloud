import mysql.connector
from DataBase.DataAccess.myConns import getMySQLConn
from DataBase.DataAccess.Database import DataBase

class mySQL(DataBase):
    myDB = getMySQLConn()
    def execModQuery(self, query: str) -> int:
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        if(self.autoCommit):
            self.myDB.commit()
        return myCursor.rowcount
    def execReadQuery(self, query: str) -> tuple:
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        return myCursor.fetchall()
    def commit(self):
        self.myDB.commit()