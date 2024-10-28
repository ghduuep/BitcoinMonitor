import requests
from datetime import datetime

def converte_timestamp(timestamp):
    timestamp_s = timestamp / 1000.0
    date_time = datetime.fromtimestamp(timestamp_s)
    return date_time.strftime('%d-%m-%Y %H:%M:%S')

def data_info():
    URL = 'https://data-api.binance.vision/api/v3/avgPrice?symbol=BTCBRL'
    
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        preco = float(data["price"])
        data_cotacao = int(data["closeTime"])
        return f'{preco:.2f}', converte_timestamp(data_cotacao)
    
    print(f'Erro {response.status_code}: Nao foi possivel continuar com a operacao')
    return
