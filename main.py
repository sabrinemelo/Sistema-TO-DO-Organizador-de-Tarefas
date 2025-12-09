def perguntar_sim_nao(mensagem):
    """Função que aceita apenas 's' ou 'n'."""
    resposta = input(mensagem).strip().lower()
    while resposta not in ['s', 'n']:
        print("Erro: digite apenas 's' para sim ou 'n' para não.")
        resposta = input(mensagem).strip().lower()
    return resposta


def adicionar_tarefa(lista_tarefas):
    """Função para adicionar tarefas validando tudo corretamente."""
    while True:
        tarefa = input("Digite a tarefa que deseja adicionar: ").strip()

        # Impedir tarefas vazias
        if tarefa == "":
            print("Erro: a tarefa não pode estar vazia!")
            continue

        lista_tarefas.append(tarefa)
        print(f"Tarefa adicionada: {tarefa}")

        # Perguntar se o usuário quer adicionar mais tarefas
        continuar = perguntar_sim_nao("Deseja adicionar outra tarefa? (s/n): ")
        if continuar == 'n':
            break


# ---------------- PROGRAMA PRINCIPAL ----------------

def main():
    tarefas = []

    print("=== SISTEMA DE GERENCIAMENTO DE TAREFAS ===")

    adicionar_tarefa(tarefas)


# Executa o programa
main()
