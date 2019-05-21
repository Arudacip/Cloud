import mysql.connector

def getMySQLConn() -> mysql.connector.connection.MySQLConnection:
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="kyN4AsHckz",
        passwd="kRLscinTnq",
        database="kyN4AsHckz"
    )
    return mydb

#Erro no MYSQL