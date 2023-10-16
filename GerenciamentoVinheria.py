from datetime import datetime

data_format = ""
tarefas = []
quantidade_tarefas = 0
data_hoje = ""

def verificar_data(a):
    print(a)
    while True:
        try:
            dia = int(input("Insira o dia: "))
            mes = int(input("Insira o mês: "))
            ano = int(input("Insira o ano: "))
            if dia > 0 and dia < 31 and mes > 0 and mes < 13 and ano >= 2023 and ano < 2100:
                data = f"{dia}/{mes}/{ano}"
                return data
            else:
                print("As datas inseridas estão inválidas! Tente novamente.")

        except:
            print("Insira apenas valores numéricos nas datas!")

def porcentagem_completude(a):
    while True:
        try:
            porcentagem = int(input(f"Insira a porcentagem de completude {a} (apenas o número): "))
            if porcentagem >= 0 and porcentagem <= 100:
                return f"{porcentagem}%"
            else:
                print("Insira um valor entre 0 e 100!")
        except:
            print("Insira uma porcentagem válida!")

def verificar_atraso():
    quantidade_tarefas_atrasadas = 0
    for i, tarefa in enumerate(tarefas,start=1):
        for chave, valor in tarefa.items():
            if chave == "Data final":
                # data_objeto = datetime.strptime(valor, "%d/%m/%Y")
                # if data_objeto < data_format:
                data_objeto = datetime.strptime(valor, "%d/%m/%Y")
                if data_objeto < datetime.strptime(data_format, "%d/%m/%Y"):
                    print("-------------------------------------")
                    print(f"Tarefa {i}")
                    if "- ATRASADO" not in tarefa["Tarefa"]:
                        tarefa["Tarefa"] += " - ATRASADO"
                    print("Tarefa: " + tarefa["Tarefa"])
                    print("Data final: " + tarefa["Data final"])
                    print("Responsável: " + tarefa["Responsável"])
                    print("Descrição: " + tarefa["Descrição"])
                    quantidade_tarefas_atrasadas += 1
    if quantidade_tarefas_atrasadas == 0:
        print("Nenhuma tarefa está atrasada no momento!")
    else:
        print(f"{quantidade_tarefas_atrasadas} tarefas de {len(tarefas)} estão constando atraso no sistema!")
    quantidade_tarefas_atrasadas = 0

def adicionar_tarefa():
    print("Você selecionou a opção 1. 'Adiconar Tarefa'!")
    tarefa = {
        "Tarefa": input("Insira o nome da tarefa: "),
        "Data inicial": verificar_data("Data inicial -"),
        "Data final": verificar_data("Data final -"),
        "Completude real": porcentagem_completude("real"),
        "Completude planejada": porcentagem_completude("planejada"),
        "Responsável": input("Nome do responsável: "),
        "Descrição": input("Insira uma descrição da tarefa: ")
    }
    tarefas.append(tarefa)
    input("A tarefa foi adicionada com sucesso! Digite qualquer caractere para voltar ao menu: ")

def exibir_tarefas():
    if len(tarefas) >0:
        for i, tarefa in enumerate(tarefas,start=1):
            print("-------------------------------------")
            print(f"Tarefa {i}")
            for chave, valor in tarefa.items():
                print(f"{chave}: {valor}")
                
    else:
        print("Não existe nenhuma tarefa registrada no sistema!")

def remover_tarefa():
    print("Você selecionou a opção 3. 'Remover Tarefa'!")
    if len(tarefas) > 0:
        while True:
            print("Das seguintes tarefas, qual o número da que você deseja remover:")
            exibir_tarefas()
            try:
                tarefa_remover = int(input("\n(Insira apenas o número da tarefa ou digite '0' para sair): "))
                if tarefa_remover >= 1 and tarefa_remover <= len(tarefas):
                    tarefas.pop(tarefa_remover - 1)
                    input("Tarefa removida com sucesso! Digite qualquer caractere para sair: ")
                    break
                elif tarefa_remover == 0:
                    print("Voltando ao menu...")
                    break
                else:
                    print("Insira uma opção válida!")
            except:
                print("Insira uma opção válida!")

    else:
        input("Para acessar este menu você precisa ter ao menos uma tarefa registrada! Digite qualquer caractere para voltar ao menu: ")


def tarefas_atrasadas():
    print("\nVocê selecionou a opção 4. 'Tarefas Atrasadas'!")
    # Colocar uma descrição na tarefa de como acelerá-la por estar atrasada
    while True:
        print("\n1. Verificar tarefas atrasadas no sistema")
        print("2. Adicionar atraso e plano de resolução manualmente")
        print("3. Sair")

        try:
            menu_tarefas_atrasadas = int(input("O que deseja fazer: "))
            match menu_tarefas_atrasadas:
                case 1:
                    verificar_atraso()
                    input("\nDigite qualquer caractere para voltar ao menu: ")
                    break
                case 2:
                    if len(tarefas) > 0:
                        while True:
                            try:
                                exibir_tarefas()
                                adicionar_plano = int(input("\nEm qual tarefa você deseja detalhar o atraso (Digite '0' para sair): "))
                                if adicionar_plano == 0:
                                    print("Voltando ao menu...")
                                    break
                                if adicionar_plano >= 1 and adicionar_plano <= len(tarefas):
                                    descricao_atraso = input("Insira um plano sucinto para resolver esse atraso: ")
                                    tarefas[adicionar_plano - 1]["Descrição do atraso"] = descricao_atraso
                                    if "- ATRASADO" not in tarefas[adicionar_plano - 1]["Tarefa"]:
                                        tarefas[adicionar_plano - 1]["Tarefa"] += "- ATRASADO"
                                    input("Plano inserido com sucesso! Digite qualquer caractere para voltar ao menu: ")
                                    break
                                else:
                                    print("Opção inválida!")
                            except:
                                print("Insira apenas o número da tarefa que deseja escolher!")
                        break
                    else:
                        input("Não existe nenhuma tarefa registrada no sistema! Insira qualquer caractere para voltar ao menu: ")
                case 3:
                    print("Voltando ao menu!")
                    break
                case _:
                    print("Insira uma opção válida!\n")
        except:
            print("Insira uma opção válida!\n")

# Início do programa
data_hoje = verificar_data("Insira a data atual -")
data_atual = datetime.strptime(data_hoje, "%d/%m/%Y")
data_format = data_atual.strftime("%d/%m/%Y")

while True:
    print("\nGERENCIAMENTO VINHERIA AGNELLO")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefa(s)")
    print("3. Remover Tarefa")
    print("4. Tarefas Atrasadas")
    print("5. Sair")
    try:
        opcao_menu = int(input("Insira o número da opção desejada: "))
        match opcao_menu:
            case 1:
                adicionar_tarefa()
            case 2:
                print("\nVocê selecionou a opção 2. 'Exibir Tarefas'!")
                exibir_tarefas()
                input("\nDigite qualquer caractere para sair: ")
            case 3:
                remover_tarefa()
            case 4:
                tarefas_atrasadas()
            case 5:
                print("Progama está sendo encerrado...")
                break
            case _:
                print("Opção inválida! Voltando ao menu...")
    
    except:
        print("Insira apenas o número da opção desejada!")