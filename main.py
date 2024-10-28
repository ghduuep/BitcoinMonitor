from scripts.sql_data import busca_dados_banco, salva_dados_banco
from scripts.data_graphic import gera_grafico
from scripts.api_data import data_info

print('Bem-vindo(a) ao Monitorador de Bitcoin (BTC)')

def menu():
    print('''
    O que voce deseja fazer?
    1 - Preco atual
    2 - Historico de precos
    3 - Gerar grafico para analise
    0 - Sair
    ''')
    escolha = int(input('Escolha: '))

    while escolha != 0:
        match escolha:
            case 1:
                dados = data_info()
                salva_dados_banco(dados)
                preco = dados[0]
                print(f'Preco atual: {preco}')
                return
            case 2:
                dados = busca_dados_banco()
                print('Preco\tData')
                print('*' * 30)
                for dado in dados:
                    print(f'{dado[1]}\t{dado[2]}')
                return
            case 3:
                gera_grafico()
                return
            case _:
                print('Opcao invalida...')
                menu()

menu()


