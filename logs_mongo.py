from db import conectar_mongo
from datetime import datetime

def listar_logs(colecao, limite=20):
    """Lista os últimos documentos de uma coleção MongoDB."""
    db = conectar_mongo()
    documentos = list(db[colecao].find().sort("timestamp", -1).limit(limite))

    if not documentos:
        print(f"  (Nenhum registo na coleção '{colecao}'.)")
        return

    print(f"\n  Últimos {len(documentos)} registos em '{colecao}':")
    print("  " + "-" * 60)
    for doc in documentos:
        ts = doc.get("timestamp", "")
        if isinstance(ts, datetime):
            ts = ts.strftime("%Y-%m-%d %H:%M:%S")
        operacao = doc.get("operacao", "—")
        dados = doc.get("dados", {})
        print(f"  [{ts}] {operacao} | {dados}")
    print()

def contar_logs(colecao):
    db = conectar_mongo()
    total = db[colecao].count_documents({})
    print(f"  Total de registos em '{colecao}': {total}")
