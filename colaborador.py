from db import conectar

class Colaborador():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def inserir(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO colaboradores (nome, email) VALUES (%s, %s)"
        valores = (self.nome, self.email)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Colaborador {self.nome} inserido na BD")
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM colaboradores")
        resultados = cursor.fetchall()

        print("\n--- Lista Completa de Colaboradores ---")
        for linha in resultados:
            print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")
            print("-------------------------\n")

        cursor.close()
        conexao.close()
    
    @staticmethod
    def atualizar(id, nome, email, self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "UPDATE colaboradores SET nome= %s, email= %s WHERE id= %s"
        cursor.execute(sql, (nome, email, id))
        conexao.commit()

        print(f"Colaborador {self.nome} atualizado com sucesso")

        cursor.close()
        conexao.close()

    @staticmethod
    def eliminar(id, self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM colaboradores WHERE id= %s", (id,))
        conexao.commit()

        print(f"Colaborador {self.nome} eliminado da BD")

        cursor.close()
        conexao.close()
