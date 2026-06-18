import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="172.234.174.181",
        port=3306,
        user="um_cbd_eder",
        password="123UM@cbd#test",
        database="mydb"
    )
    return conexao

conn = conectar()