import os
from cliente import Cliente
from colaborador import Colaborador
from departamento import Departamento
from conta import Conta
from logs_mongo import listar_logs, contar_logs

# ──────────────────────────────────────────────
# Utilitários de interface
# ──────────────────────────────────────────────
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n  Pressione Enter para continuar...")

def cabecalho(titulo):
    limpar()
    print("=" * 50)
    print(f"  SGB – Sistema de Gestão Bancária")
    print(f"  {titulo}")
    print("=" * 50)

def ler_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Introduza um número inteiro válido.")

def ler_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Introduza um valor numérico válido.")

# ──────────────────────────────────────────────
# Gestão de Clientes
# ──────────────────────────────────────────────
def menu_clientes():
    while True:
        cabecalho("Gestão de Clientes")
        print("  1. Listar Clientes")
        print("  2. Inserir Novo Cliente")
        print("  3. Editar Cliente")
        print("  4. Eliminar Cliente")
        print("  0. Voltar")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            cabecalho("Lista de Clientes")
            Cliente.listar()
            pausar()

        elif opcao == "2":
            cabecalho("Inserir Cliente")
            nome = input("  Nome: ").strip()
            email = input("  Email: ").strip()
            if nome and email:
                Cliente(nome, email).inserir()
            else:
                print("  Nome e email são obrigatórios.")
            pausar()

        elif opcao == "3":
            cabecalho("Editar Cliente")
            Cliente.listar()
            id = ler_int("  ID do cliente a editar: ")
            nome = input("  Novo nome: ").strip()
            email = input("  Novo email: ").strip()
            if nome and email:
                Cliente.atualizar(id, nome, email)
            else:
                print("  Nome e email são obrigatórios.")
            pausar()

        elif opcao == "4":
            cabecalho("Eliminar Cliente")
            Cliente.listar()
            id = ler_int("  ID do cliente a eliminar: ")
            confirmar = input(f"  Confirmar eliminação do cliente ID {id}? (s/n): ").strip().lower()
            if confirmar == "s":
                Cliente.eliminar(id)
            else:
                print("  Operação cancelada.")
            pausar()

        elif opcao == "0":
            break

# ──────────────────────────────────────────────
# Gestão de Colaboradores
# ──────────────────────────────────────────────
def menu_colaboradores():
    while True:
        cabecalho("Gestão de Colaboradores")
        print("  1. Listar Colaboradores")
        print("  2. Inserir Novo Colaborador")
        print("  3. Editar Colaborador")
        print("  4. Eliminar Colaborador")
        print("  0. Voltar")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            cabecalho("Lista de Colaboradores")
            Colaborador.listar()
            pausar()

        elif opcao == "2":
            cabecalho("Inserir Colaborador")
            nome = input("  Nome: ").strip()
            email = input("  Email: ").strip()
            if nome and email:
                Colaborador(nome, email).inserir()
            else:
                print("  Nome e email são obrigatórios.")
            pausar()

        elif opcao == "3":
            cabecalho("Editar Colaborador")
            Colaborador.listar()
            id = ler_int("  ID do colaborador a editar: ")
            nome = input("  Novo nome: ").strip()
            email = input("  Novo email: ").strip()
            if nome and email:
                Colaborador.atualizar(id, nome, email)
            else:
                print("  Nome e email são obrigatórios.")
            pausar()

        elif opcao == "4":
            cabecalho("Eliminar Colaborador")
            Colaborador.listar()
            id = ler_int("  ID do colaborador a eliminar: ")
            confirmar = input(f"  Confirmar eliminação do colaborador ID {id}? (s/n): ").strip().lower()
            if confirmar == "s":
                Colaborador.eliminar(id)
            else:
                print("  Operação cancelada.")
            pausar()

        elif opcao == "0":
            break

# ──────────────────────────────────────────────
# Gestão de Departamentos
# ──────────────────────────────────────────────
def menu_departamentos():
    while True:
        cabecalho("Gestão de Departamentos")
        print("  1. Listar Departamentos")
        print("  2. Inserir Novo Departamento")
        print("  3. Editar Departamento")
        print("  4. Eliminar Departamento")
        print("  0. Voltar")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            cabecalho("Lista de Departamentos")
            Departamento.listar()
            pausar()

        elif opcao == "2":
            cabecalho("Inserir Departamento")
            nome = input("  Nome: ").strip()
            if nome:
                Departamento(nome).inserir()
            else:
                print("  O nome é obrigatório.")
            pausar()

        elif opcao == "3":
            cabecalho("Editar Departamento")
            Departamento.listar()
            id = ler_int("  ID do departamento a editar: ")
            nome = input("  Novo nome: ").strip()
            if nome:
                Departamento.atualizar(id, nome)
            else:
                print("  O nome é obrigatório.")
            pausar()

        elif opcao == "4":
            cabecalho("Eliminar Departamento")
            Departamento.listar()
            id = ler_int("  ID do departamento a eliminar: ")
            confirmar = input(f"  Confirmar eliminação do departamento ID {id}? (s/n): ").strip().lower()
            if confirmar == "s":
                Departamento.eliminar(id)
            else:
                print("  Operação cancelada.")
            pausar()

        elif opcao == "0":
            break

# ──────────────────────────────────────────────
# Gestão de Contas
# ──────────────────────────────────────────────
def menu_contas():
    while True:
        cabecalho("Gestão de Contas")
        print("  1. Listar Contas")
        print("  2. Criar Nova Conta")
        print("  3. Depositar")
        print("  4. Levantar")
        print("  5. Eliminar Conta")
        print("  0. Voltar")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            cabecalho("Lista de Contas")
            Conta.listar()
            pausar()

        elif opcao == "2":
            cabecalho("Criar Conta")
            Cliente.listar()
            cliente_id = ler_int("  ID do cliente: ")
            print("  Tipos disponíveis: Corrente | Poupança")
            tipo = input("  Tipo de conta: ").strip()
            saldo = ler_float("  Saldo inicial (CVE): ")
            Conta(cliente_id, tipo, saldo).inserir()
            pausar()

        elif opcao == "3":
            cabecalho("Depositar")
            Conta.listar()
            id = ler_int("  ID da conta: ")
            valor = ler_float("  Valor a depositar (CVE): ")
            Conta.depositar(id, valor)
            pausar()

        elif opcao == "4":
            cabecalho("Levantar")
            Conta.listar()
            id = ler_int("  ID da conta: ")
            valor = ler_float("  Valor a levantar (CVE): ")
            Conta.levantar(id, valor)
            pausar()

        elif opcao == "5":
            cabecalho("Eliminar Conta")
            Conta.listar()
            id = ler_int("  ID da conta a eliminar: ")
            confirmar = input(f"  Confirmar eliminação da conta ID {id}? (s/n): ").strip().lower()
            if confirmar == "s":
                Conta.eliminar(id)
            else:
                print("  Operação cancelada.")
            pausar()

        elif opcao == "0":
            break

# ──────────────────────────────────────────────
# Logs MongoDB
# ──────────────────────────────────────────────
def menu_logs():
    while True:
        cabecalho("Registos MongoDB")
        print("  1. Ver logs de transações (depósitos/levantamentos)")
        print("  2. Ver logs de auditoria (criações/edições/eliminações)")
        print("  3. Contar registos")
        print("  0. Voltar")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            cabecalho("Logs – Transações")
            listar_logs("transacoes")
            pausar()

        elif opcao == "2":
            cabecalho("Logs – Auditoria")
            listar_logs("auditoria")
            pausar()

        elif opcao == "3":
            cabecalho("Contagem de Registos MongoDB")
            contar_logs("transacoes")
            contar_logs("auditoria")
            pausar()

        elif opcao == "0":
            break

# ──────────────────────────────────────────────
# Menu Principal
# ──────────────────────────────────────────────
def main():
    while True:
        cabecalho("Menu Principal")
        print("  1. Gestão de Clientes")
        print("  2. Gestão de Colaboradores")
        print("  3. Gestão de Departamentos")
        print("  4. Gestão de Contas")
        print("  5. Registos / Logs (MongoDB)")
        print("  0. Sair")
        opcao = input("\n  Opção: ").strip()

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_colaboradores()
        elif opcao == "3":
            menu_departamentos()
        elif opcao == "4":
            menu_contas()
        elif opcao == "5":
            menu_logs()
        elif opcao == "0":
            limpar()
            print("  Até logo!")
            break
        else:
            print("  Opção inválida.")
            pausar()

if __name__ == "__main__":
    main()
