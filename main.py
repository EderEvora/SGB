from cliente import Cliente
from colaborador import Colaborador

def exibir_menu():
    print("=== Sistema Bancário ===")
    print("1. Gestão de Clientes")
    print("2. Gestão de Colaboradores")
    print("3. Gestão de Departamentos")
    print("4. Gestão de Contas")
    print("5. Configuração do Banco/App")
    print("0. Sair do Aplicativo")

def menu_clientes():
    print("1. Listar Clientes ")
    print("2. Inserir Novo Cliente ")
    print("3. Editar Cliente ")
    print("4. Eliminar Cliente ")
    print("0. Voltar ao Menu Principal ")

def gestao_clientes():
    while True:
        menu_clientes()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            Cliente.listar()

        elif opcao == '2':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            novo_cliente = Cliente(nome, email)
            novo_cliente.inserir()

        elif opcao == '3':
            id = input("Digite o id: ")
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            Cliente.atualizar(id, nome, email)

        elif opcao == '4':
            id = input("Digite o id: ")
            Cliente.eliminar(id)

        elif opcao == '0':
            print("Voltando para Menu Inicial")
            break
        else:
            print("Opção inválida")

def menu_colaboradores():
    print("1.1. Listar Colaboradores ")
    print("1.2. Inserir Novo Colaborador ")
    print("1.3. Editar Colaborador ")
    print("1.4. Eliminar Colaborador ")
    print("0. Voltar ao Menu Principal ")

def gestao_colaboradores():
    while True:
        menu_colaboradores()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            Colaborador.listar()

        elif opcao == '2':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            novo_colaborador = Colaborador(nome, email)
            novo_colaborador.inserir()

        elif opcao == '3':
            id = input("Digite o id: ")
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            Colaborador.atualizar(id, nome, email)

        elif opcao == '4':
            id = input("Digite o id: ")
            Colaborador.eliminar(id)

        elif opcao == '0':
            print("Voltando para Menu Inicial")
            break
        else:
            print("Opção inválida")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gestao_clientes()

        elif opcao == '2':
            gestao_colaboradores()

        elif opcao == '0':
            print("Saindo do App")
            break 

        else:
            print("Nana")

if __name__ == "__main__":
    main()