lista_colaboradores = []

# Variável global para IDs
id_global = 0

# Função para cadastrar colaborador.
def cadastrar_colaborador(id):
    print(' ---------- Bem-vindos ao cadastro de colaborador ----------\n')
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))
    colaborador = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_colaboradores.append(colaborador)

# Função para consultar os colaboradores.
def consultar_colaborador():
    print(' ---------- Bem-vindo ao menu de consulta de colaborador ----------\n')
    opcao = int(input(
        "Escolha uma opção:\n"
        "1 - Consultar Todos\n"
        "2 - Consultar por Id\n"
        "3 - Consultar por Setor\n"
        "4 - Retornar ao menu\n"
        ">>"))

    if opcao == 1:
        print("Todos os colaboradores:")
        for colaborador in lista_colaboradores:
            print(colaborador)
    elif opcao == 2:
        id_consulta = int(input("Digite o ID do colaborador: "))
        for colaborador in lista_colaboradores:
            if colaborador['id'] == id_consulta:
                print("Colaborador encontrado:")
                print(colaborador)
                break
        else:
            print("Colaborador não encontrado.")
    elif opcao == 3:
        setor_consulta = input("Digite o setor a ser consultado: ")
        print(f"Colaboradores do setor {setor_consulta}:")
        for colaborador in lista_colaboradores:
            if colaborador['setor'] == setor_consulta:
                print(colaborador)
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")

# Função para remover colaborador.
def remover_colaborador():
    id_remocao = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_remocao:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido.")
            break
    else:
        print("Colaborador não encontrado.")

# Função Principal.
def main():
    print("Bem-vindo ao software de gerenciamento de pessoas do Wylker Aparecido Peres Goulart!")
    while True:
        opcao_menu = int(input("\nEscolha uma opção:\n"
                               "1. Cadastrar Colaborador\n"
                               "2. Consultar Colaborador\n"
                               "3. Remover Colaborador\n"
                               "4. Encerrar Programa\n"
                               ">>"))

        if opcao_menu == 1:
            global id_global
            id_global += 1
            cadastrar_colaborador(id_global)
        elif opcao_menu == 2:
            consultar_colaborador()
        elif opcao_menu == 3:
            remover_colaborador()
        elif opcao_menu == 4:
            print("Obrigado por usar nossos sistemas.")
            break
        else:
            print("Opção inválida. Digite uma das opções acima.")

# Iniciar o programa.
main()

# Cadastro de 3 colaboradores.
for _ in range(3):
    id_global += 1
    cadastrar_colaborador(id_global)
