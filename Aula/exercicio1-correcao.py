# 1 - faltam as aspas, e em um cógigo normal, não vamos executar essa linhar
print("Bem-vindo à sua lista de tarefas!")

# 2 - Variável global, não é recomendavel
# Deveria ser uma lista
tarefas = []

def adicionar_tarefa():
    # 3 - Parenteses extras no input
    nova_tarefa = input("Digite a nova tarefa: ")
    # 4 - Erro ao adicionar o item
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso.")

def ver_tarefas():
    print("\nSuas tarefas:")
    # 5 for in range é o correto, quebrando o modo pytonico
    # Pep 8
    try:
        for letra in tarefas:
            # 6 - temos 2 erros aqui
            print(letra)
    except TypeError:
        print("Erro de tipo")
        raise

def remover_tarefa():
    ver_tarefas()
    try:
        # 7 - Não valido o tipo do input
        indice_input = input("Digite o número da tarefa a ser removida: ")
        indice = int(indice_input) - 1

        # 8 - Antes estava atuando sobre um string, agora é uma lista
        del tarefas[indice]
        print("Tarefa removida com sucesso!")
    except TypeError as e:
        print("Erro de tipo ao remover tarefa:", e)
    except Exception as e:
        # 9 - Exception genérica, devemos ter outras excessões mais especificas
        print("Erro ao remover tarefa:", e)
    
# 10 - Erro de nome, função sempre com minusculo
def menu():
    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        try:
            escolha = int(input("Escolha uma opção: "))

            # Deveria ser um switch case

            # match escolha:
            #     case 1:
            #         return adicionar_tarefa()
            #     case 2:
            #         return ver_tarefas()
            #     case 3:
            #         return remover_tarefa()
            #     case 4:
            #         return
            #     case _:
            #         print("Opção inválida. Tente novamente.")


            if escolha == 1: # 11 apenas um = em um comparação
                adicionar_tarefa()
            elif escolha == 2:
                ver_tarefas()
            elif escolha == 3:
                remover_tarefa()
            elif escolha == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError as e:
            print("Erro de valor no menu: ", e)
            continue


# Chamada para iniciar o programa
# 12 - name main

if __name__ == '__main__':
    menu()
