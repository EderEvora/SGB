from db import conectar

class Cliente():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def inserir(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        valores = (self.nome, self.email)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Cliente {self.nome} inserido na BD")
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM clientes")
        resultados = cursor.fetchall()

        print("\n--- Lista Completa de Clientes ---")
        for linha in resultados:
            print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")
            print("-------------------------\n")

        cursor.close()
        conexao.close()
    
    @staticmethod
    def atualizar(id, nome, email, self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "UPDATE clientes SET nome= %s, email= %s WHERE id= %s"
        cursor.execute(sql, (nome, email, id))
        conexao.commit()

        print(f"Cliente {self.nome} atualizado com sucesso")

        cursor.close()
        conexao.close()

    @staticmethod
    def eliminar(id, self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM clientes WHERE id= %s", (id,))
        conexao.commit()

        print(f"Cliente {self.nome} eliminado da BD")

        cursor.close()
        conexao.close()
cl1 = Cliente("Ana Paula", "anapaula@gmail.com")

cl1.inserir()