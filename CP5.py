# zfill() preenche uma string com zeros, sendo útil para formatar datas por exemplo
import datetime

tarefas = []

def verificar_data(a):
    print(a)
    try:
        dia = int(input("Insira o dia: "))
        mes = int(input("Insira o mês: "))
        ano = int(input("Insira o ano: "))
        data_formatada = f"{dia}/{mes}/{ano}"

    except:
        print("")

def adicionar_tarefa():
    print("Você selecionou a opção 1. 'Adiconar Tarefa'!")
    tarefa = {
        "Nome da tarefa": input("Insira o nome da tarefa"),
        "Data inicial": verificar_data("Data inicial:")
    }

def exibir_tarefas():
    print("Você selecionou a opção 2. 'Exibir Tarefas'!")

def tarefas_atrasadas():
    print("Você selecionou a opção 3. 'Tarefas Atrasadas'!")

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
