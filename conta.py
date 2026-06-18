from db import conectar_mysql, registar_log

class Conta:
    def __init__(self, cliente_id, tipo, saldo=0.00):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.saldo = saldo

    def inserir(self):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        sql = "INSERT INTO contas (cliente_id, tipo, saldo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.cliente_id, self.tipo, self.saldo))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"  Conta '{self.tipo}' criada para o cliente ID {self.cliente_id} (Conta ID: {novo_id}).")
        cursor.close()
        conexao.close()
        registar_log("transacoes", "criar_conta", {
            "conta_id": novo_id,
            "cliente_id": self.cliente_id,
            "tipo": self.tipo,
            "saldo_inicial": float(self.saldo)
        })

    @staticmethod
    def listar():
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT c.id, cl.nome, c.tipo, c.saldo
            FROM contas c
            JOIN clientes cl ON c.cliente_id = cl.id
            ORDER BY c.id
        """)
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        if not resultados:
            print("  (Nenhuma conta registada.)")
            return

        print(f"\n  {'ID':<5} {'Cliente':<25} {'Tipo':<15} {'Saldo (CVE)'}")
        print("  " + "-" * 60)
        for linha in resultados:
            print(f"  {linha[0]:<5} {linha[1]:<25} {linha[2]:<15} {float(linha[3]):,.2f}")
        print()

    @staticmethod
    def depositar(id, valor):
        if valor <= 0:
            print("  O valor do depósito deve ser positivo.")
            return
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("UPDATE contas SET saldo = saldo + %s WHERE id = %s", (valor, id))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Conta ID {id} não encontrada.")
        else:
            print(f"  Depósito de {valor:,.2f} CVE realizado na conta ID {id}.")
            registar_log("transacoes", "deposito", {"conta_id": id, "valor": float(valor)})

    @staticmethod
    def levantar(id, valor):
        if valor <= 0:
            print("  O valor do levantamento deve ser positivo.")
            return
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("SELECT saldo FROM contas WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        if not resultado:
            print(f"  Conta ID {id} não encontrada.")
            cursor.close()
            conexao.close()
            return

        saldo_atual = float(resultado[0])
        if valor > saldo_atual:
            print(f"  Saldo insuficiente. Saldo atual: {saldo_atual:,.2f} CVE.")
            cursor.close()
            conexao.close()
            return

        cursor.execute("UPDATE contas SET saldo = saldo - %s WHERE id = %s", (valor, id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"  Levantamento de {valor:,.2f} CVE realizado na conta ID {id}.")
        registar_log("transacoes", "levantamento", {"conta_id": id, "valor": float(valor)})

    @staticmethod
    def eliminar(id):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM contas WHERE id=%s", (id,))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Conta ID {id} não encontrada.")
        else:
            print(f"  Conta ID {id} eliminada.")
            registar_log("auditoria", "eliminar_conta", {"conta_id": id})
