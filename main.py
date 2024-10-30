from scripts.sql_data import busca_dados_banco, salva_dados_banco
from scripts.data_graphic import gera_grafico
from scripts.api_data import data_info
from scripts.news_data import gera_noticias
import time

print('Bem-vindo(a) ao Monitorador de Bitcoin (BTC)')

def menu():
    escolha = None

    while escolha != 0:
        print('''
O que voce deseja fazer?
1 - Preco atual
2 - Historico de precos
3 - Gerar grafico para analise
4 - Ver noticias
0 - Sair
        ''')
        escolha = int(input('Escolha: '))

        match escolha:
            case 1:
                dados = data_info()
                salva_dados_banco(dados)
                preco = dados[0]
                print(f'Preco atual: {preco}')
                time.sleep(2)
            case 2:
                dados = busca_dados_banco()
                print('Preco\tData')
                print('*' * 30)
                for dado in dados:
                    print(f'{dado[1]}\t{dado[2]}')
                time.sleep(2)
            case 3:
                gera_grafico()
                time.sleep(2)
            case 4:
                print('Aqui estão as ultimas notícias relacionadas ao BTC')
                print('-' * 30)
                noticias = gera_noticias()
                for noticia in noticias:
                    print(noticia, '\n')
             
                time.sleep(2)
            case 0:
                print('Saindo do programa...')
            case _:
                print('Opcao invalida...')

menu()


