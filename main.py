def definir_prioridade():
    global tarefas
    if len(tarefas) == 0:
        print("Não há tarefas para definir prioridade.\n")
        return

    # Mostrar lista de tarefas antes de escolher
    print("\n=== TAREFAS DISPONÍVEIS ===")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['nome']}")
    print("===========================\n")

    # Escolher tarefa
    escolha = input("Qual tarefa você quer definir a prioridade? (Digite o número): ")
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(tarefas):
        print("Escolha inválida.\n")
        return
    
    tarefa = tarefas[int(escolha) - 1]

    # Escolher nova prioridade
    print("Escolha a prioridade:")
    print("1. Alta")   
    print("2. Média")
    print("3. Baixa")
    opcao = input("Digite o número da prioridade: ")
    
    if opcao == '1':
        tarefa['prioridade'] = 'Alta'
        tarefa['peso'] = 3
    elif opcao == '2':
        tarefa['prioridade'] = 'Média'
        tarefa['peso'] = 2
    else:
        tarefa['prioridade'] = 'Baixa'
        tarefa['peso'] = 1

    print(f"Prioridade da tarefa '{tarefa['nome']}' definida como {tarefa['prioridade']}.\n")

def marcar_tarefa_como_concluida(tarefas):
    print("\nLista de tarefas:")
    for i in range(len(tarefas)):
        print(f"{i+1}. {tarefas[i]}")

    escolha = int(input("\nDigite o número da tarefa concluída: ")) - 1

    if 0 <= escolha < len(tarefas):
        tarefa = tarefas.pop(escolha)
        print(f"\nTarefa concluída: {tarefa}")
    else:
        print("\nNúmero inválido")
