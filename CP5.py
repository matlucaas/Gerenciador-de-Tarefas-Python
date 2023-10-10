# zfill() preenche uma string com zeros, sendo útil para formatar datas por exemplo

tarefas = []

def verificar_data(a):
    print(a)
    while True:
        try:
            dia = int(input("Insira o dia: "))
            mes = int(input("Insira o mês: "))
            ano = int(input("Insira o ano: "))
            if dia > 0 and dia < 31 and mes > 0 and mes < 13 and ano >= 2023:
                data = [dia, mes, ano]
                return data
            else:
                print("As datas inseridas estão inválidas! Tente novamente.")

        except:
            print("Insira apenas valores numéricos nas datas!")

def porcentagem_completude(a):
    print(a)
    while True:
        try:
            porcentagem = int(input("Insira a porcentagem de completude real: "))
            if porcentagem >= 0 and porcentagem <= 100:
                return porcentagem
            else:
                print("Insira um valor entre 0 e 100!")
        except:
            print("Insira uma porcentagem válida!")

def adicionar_tarefa():
    print("Você selecionou a opção 1. 'Adiconar Tarefa'!")
    tarefa = {
        "tarefa": input("Insira o nome da tarefa"),
        "data_inicial": verificar_data("Data inicial:"),
        "data_final": verificar_data("Data final:"),
        "completude_real": porcentagem_completude("Porcentagem completude real"),
        "completude_planejada": porcentagem_completude("Porcentagem completude planejada"),
        "responsavel": input("Nome do responsável: "),
        "descricao": input("Insira uma descrição da tarefa")
    }
    tarefas.append(tarefa)
    print("A tarefa foi adicionada com sucesso!")

def exibir_tarefas():
    print("Você selecionou a opção 2. 'Exibir Tarefas'!")
    for i in tarefas:
        for tarefa in i:
            print(tarefa)

def tarefas_atrasadas():
    print("Você selecionou a opção 3. 'Tarefas Atrasadas'!")

# Início do programa

dia_atual = int(input("Insira a data de hoje:\nDia: "))
mes_atual = int(input("Mês: "))
ano_atual = int(input("Ano: "))

while True:
    print("GERENCIAMENTO VINHERIA AGNELLO")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefa(s)")
    print("3. Tarefas Atrasadas")
    print("4. Sair")
    opcao_menu = int(input("Insira o número da opção desejada: "))

    match opcao_menu:
        case 1:
            adicionar_tarefa()
        case 2:
            exibir_tarefas()
        case 3: 
            tarefas_atrasadas()
        case 4:
            break
        case _:
            print("Opção inválida! Voltando ao menu...")
