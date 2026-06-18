from db import conectar_mysql, registar_log

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def inserir(self):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        cursor.execute(sql, (self.nome, self.email))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"  Cliente '{self.nome}' inserido com sucesso (ID: {novo_id}).")
        cursor.close()
        conexao.close()
        registar_log("auditoria", "criar_cliente", {"id": novo_id, "nome": self.nome, "email": self.email})

    @staticmethod
    def listar():
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM clientes ORDER BY id")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        if not resultados:
            print("  (Nenhum cliente registado.)")
            return

        print(f"\n  {'ID':<5} {'Nome':<30} {'Email'}")
        print("  " + "-" * 60)
        for linha in resultados:
            print(f"  {linha[0]:<5} {linha[1]:<30} {linha[2]}")
        print()

    @staticmethod
    def atualizar(id, nome, email):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        sql = "UPDATE clientes SET nome=%s, email=%s WHERE id=%s"
        cursor.execute(sql, (nome, email, id))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Nenhum cliente com ID {id} encontrado.")
        else:
            print(f"  Cliente ID {id} atualizado com sucesso.")
            registar_log("auditoria", "atualizar_cliente", {"id": id, "nome": nome, "email": email})

    @staticmethod
    def eliminar(id):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Nenhum cliente com ID {id} encontrado.")
        else:
            print(f"  Cliente ID {id} eliminado.")
            registar_log("auditoria", "eliminar_cliente", {"id": id})
