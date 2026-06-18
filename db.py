import mysql.connector
from pymongo import MongoClient
from datetime import datetime
import dotenv
import os

dotenv.load_dotenv()


# Conexão MySQL

def conectar_mysql():
    conexao = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
    )
    return conexao


# Conexão MongoDB

def conectar_mongo():
    # Retorna a base de dados MongoDB 'sgb_logs'.
    cliente = MongoClient("mongodb://localhost:27017/")
    return cliente["sgb_logs"]


# Registar log no MongoDB

def registar_log(colecao: str, operacao: str, dados: dict):
    
    # Regista um documento de auditoria na coleção indicada do MongoDB.
    # Parâmetros:
    #    colecao  – nome da coleção (ex: 'transacoes', 'auditoria')
    #    operacao – descrição da ação (ex: 'deposito', 'criar_conta')
    #    dados    – dicionário com detalhes relevantes

    try:
        db = conectar_mongo()
        documento = {
            "operacao": operacao,
            "dados": dados,
            "timestamp": datetime.now()
        }
        db[colecao].insert_one(documento)
    except Exception as e:
        # Falha no MongoDB nunca deve interromper a operação principal
        print(f"  [Aviso] Não foi possível registar log MongoDB: {e}")
