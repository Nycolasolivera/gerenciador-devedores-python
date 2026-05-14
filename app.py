import json
import os

DEVEDORES = {}

def adicionar_devedor():
    titulo_limpar_tela("Criar novo devedor")
    devedor = input("Digite o nome do devedor: ").strip().title()

    if not devedor:
        print("O nome não pode ser vazio!")
        input("\nPressione ENTER para continuar...")
        return

    if devedor in DEVEDORES:
        print(f'O devedor "{devedor}" já existe!')
        input("\nPressione ENTER para continuar...")
        return

    DEVEDORES[devedor] = []
    print(f'Devedor {devedor} criado com sucesso!!')
    salvar_dados(DEVEDORES)
    input("\nPressione ENTER para continuar...")

def adicionar_divida():
    titulo_limpar_tela('A dicionar divida')
    devedor = str(input('digite o nome do devedor que ira adicionar a divida: ')).strip().title()

    if devedor not in DEVEDORES:
        titulo_limpar_tela('Devedor não encontrado!')
        input("\nPressione ENTER para continuar...")
        return
    
    while True:
        titulo_limpar_tela(f'Adicionar divida de {devedor}')
        try:
            valor = float(input('Digite o valor a pagar: '))
        except ValueError:
            print("Por favor, digite apenas números.")
            input("Pressione Enter para tentar novamente...")
            continue       
        DEVEDORES[devedor].append(valor)
        salvar_dados(DEVEDORES)

        loop = input("Pressione ENTER para continuar...\nDigite 1 para voltar ao menu: ")

        if loop == "1":
            break

def adicionar_pagamento():
    titulo_limpar_tela('Adicionar Pagamento')
    devedor = str(input('digite o nome do devedor que ira pagar a divida: ')).strip().title()

    if devedor not in DEVEDORES:
        titulo_limpar_tela("Devedor não encontrado!")
        input("\nPressione ENTER para continuar...")
        return
    
    while True:
        titulo_limpar_tela(f'Adicionar pagamento de {devedor}')
        try:
            valor = float(input('Digite o valor a pagar: '))
        except ValueError:
            print("Por favor, digite apenas números.")
            input("Pressione Enter para tentar novamente...")
            continue
        DEVEDORES[devedor].append(-valor)
        salvar_dados(DEVEDORES)

        loop = input("Pressione ENTER para continuar...\nDigite 1 para voltar ao menu: ")

        if loop == "1":
            break

def ver_extrato():
    titulo_limpar_tela('Visualizar Extratos')
    devedor = str(input('digite o nome do devedor que para ver o extrato: ')).strip().title()

    if devedor not in DEVEDORES:
        print("Devedor não encontrado!")
        input("Pressione ENTER para continuar...")
        return
    
    dividas = DEVEDORES[devedor]

    if not dividas:
        print("Este devedor não possui dívidas.")
    else:
        print(f"\nExtrato de {devedor}:\n")
        for i, valor in enumerate(dividas, 1):
            print(f"{i}. R$ {valor:.2f}")

        print(f"\nTotal da dívida: R$ {sum(dividas):.2f}")
        input("\nPressione ENTER para continuar...")

# funcoes de manipulaçoa de dados
def salvar_dados(dicionario):
    with open('dados_usuarios.json', 'w', encoding='utf-8') as f:
        json.dump(dicionario, f, indent=4, ensure_ascii=False)

def carregar_dados():
    global DEVEDORES
    try:
        with open('dados_usuarios.json', 'r', encoding='utf-8') as f:
            DEVEDORES = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        DEVEDORES = {}

#funçoes de menu
def titulo_limpar_tela(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""                                 _           _               __ _                            _           
                                (_)         | |             / _(_)                          (_)          
   __ _  ___ _ __ ___ _ __   ___ _  __ _  __| | ___  _ __  | |_ _ _ __   __ _ _ __   ___ ___ _ _ __ ___  
  / _` |/ _ \ '__/ _ \ '_ \ / __| |/ _` |/ _` |/ _ \| '__| |  _| | '_ \ / _` | '_ \ / __/ _ \ | '__/ _ \ 
 | (_| |  __/ | |  __/ | | | (__| | (_| | (_| | (_) | |    | | | | | | | (_| | | | | (_|  __/ | | | (_) |
  \__, |\___|_|  \___|_| |_|\___|_|\__,_|\__,_|\___/|_|    |_| |_|_| |_|\__,_|_| |_|\___\___|_|_|  \___/ 
   __/ |                                                                                                 
  |___/                                                                                                   
          """)
    print(texto)

def main():
    carregar_dados()
    print(DEVEDORES)

    while True:
        titulo_limpar_tela("Menu")
        print('1. Criar novo devedor')
        print('2. adicionar divida')
        print('3. pagar divida')
        print('4. ver extrato')
        print('5. Sair\n')

        opcao = input('Escolha uma opção: ')
        print('Você escolheu a opção: ', opcao)

        if opcao == '1':
            print('Cadastras devedor')
            adicionar_devedor()

        elif opcao == '2':
            print('Adicionar divida')
            adicionar_divida()

        elif opcao == '3':
            print('pagar divida')
            adicionar_pagamento()

        elif opcao == '4':
            print('ver extrato')
            ver_extrato()

        elif opcao == '5':
            print("Encerrando programa...")
            break
        
        else:
            print('A opção escolhida é inválida')
            input("\nPressione ENTER para continuar...")

if __name__ == '__main__':
    main()
