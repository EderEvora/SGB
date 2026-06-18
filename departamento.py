from db import conectar

class Departamento():
    def __init__(self, nome):
        self.nome = nome

    def inserir(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO departamentos (nome) VALUES (%s)"
        cursor.execute(sql, (self.nome,))
        conexao.commit()
        print(f"Departamento {self.nome} inserido com sucesso!")
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM departamentos")
        resultados = cursor.fetchall()

        print("\n--- Lista de Departamentos ---")
        for linha in resultados:
            print(f"ID: {linha[0]} | Nome: {linha[1]}")
        print("-------------------------\n")

        cursor.close()
        conexao.close()

    @staticmethod
    def atualizar(id, nome):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "UPDATE departamentos SET nome = %s WHERE id = %s"
        cursor.execute(sql, (nome, id))
        conexao.commit()
        print(f"Departamento ID {id} atualizado com sucesso!")
        cursor.close()
        conexao.close()

    @staticmethod
    def eliminar(id):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM departamentos WHERE id = %s", (id,))
        conexao.commit()
        print(f"Departamento ID {id} eliminado com sucesso!")
        cursor.close()
        conexao.close()
