from db import conectar_mysql, registar_log

class Departamento:
    def __init__(self, nome):
        self.nome = nome

    def inserir(self):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        sql = "INSERT INTO departamentos (nome) VALUES (%s)"
        cursor.execute(sql, (self.nome,))
        conexao.commit()
        novo_id = cursor.lastrowid
        print(f"  Departamento '{self.nome}' criado com sucesso (ID: {novo_id}).")
        cursor.close()
        conexao.close()
        registar_log("auditoria", "criar_departamento", {"id": novo_id, "nome": self.nome})

    @staticmethod
    def listar():
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM departamentos ORDER BY id")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        if not resultados:
            print("  (Nenhum departamento registado.)")
            return

        print(f"\n  {'ID':<5} {'Nome'}")
        print("  " + "-" * 40)
        for linha in resultados:
            print(f"  {linha[0]:<5} {linha[1]}")
        print()

    @staticmethod
    def atualizar(id, nome):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        sql = "UPDATE departamentos SET nome=%s WHERE id=%s"
        cursor.execute(sql, (nome, id))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Nenhum departamento com ID {id} encontrado.")
        else:
            print(f"  Departamento ID {id} atualizado.")
            registar_log("auditoria", "atualizar_departamento", {"id": id, "nome": nome})

    @staticmethod
    def eliminar(id):
        conexao = conectar_mysql()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM departamentos WHERE id=%s", (id,))
        conexao.commit()
        linhas = cursor.rowcount
        cursor.close()
        conexao.close()

        if linhas == 0:
            print(f"  Nenhum departamento com ID {id} encontrado.")
        else:
            print(f"  Departamento ID {id} eliminado.")
            registar_log("auditoria", "eliminar_departamento", {"id": id})
