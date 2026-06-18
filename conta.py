from db import conectar

class Conta():
    def __init__(self, cliente_id, tipo, saldo):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.saldo = saldo

    def inserir(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO contas (cliente_id, tipo, saldo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.cliente_id, self.tipo, self.saldo))
        conexao.commit()
        print(f"Conta do tipo {self.tipo} criada com sucesso!")
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, cliente_id, tipo, saldo FROM contas")
        resultados = cursor.fetchall()

        print("\n--- Lista de Contas ---")
        for linha in resultados:
            print(f"ID: {linha[0]} | Cliente ID: {linha[1]} | Tipo: {linha[2]} | Saldo: {linha[3]}")
        print("-------------------------\n")

        cursor.close()
        conexao.close()

    @staticmethod
    def atualizar(id, tipo, saldo):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "UPDATE contas SET tipo = %s, saldo = %s WHERE id = %s"
        cursor.execute(sql, (tipo, saldo, id))
        conexao.commit()
        print(f"Conta ID {id} atualizada com sucesso!")
        cursor.close()
        conexao.close()

    @staticmethod
    def eliminar(id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM contas WHERE id = %s", (id,))
        conexao.commit()
        print(f"Conta ID {id} eliminada com sucesso!")
        cursor.close()
        conexao.close()
