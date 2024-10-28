import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .sql_data import busca_dados_banco
from datetime import datetime
import os

dados = busca_dados_banco()

precos = []
datas = []

def gera_grafico():
    for dado in dados:
        preco = dado[1]
        data = dado[2]
        precos.append(preco)
        datas.append(data)

    plt.plot(datas, precos)
    plt.xlabel('Datas')
    plt.ylabel('Preco em BRL')
    plt.title('Preco do Bitcoin (BTC)')

    diretorio = f'/home/{os.getlogin()}/Imagens'

    if not os.path.exists(diretorio):
        os.makedirs(diretorio, exist_ok=True)
        print('Diretorio criado com sucesso!')
    print('O diretorio ja existe.')
    print('Salvando grafico no seu diretorio de Imagens!')

    plt.savefig(os.path.join(diretorio, f'grafico-btc-{datetime.now().strftime('%d-%m-%Y - %H:%M:%S')}.png'))


