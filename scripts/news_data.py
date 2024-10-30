import requests
from bs4 import BeautifulSoup

def gera_noticias():
    URL = 'https://www.binance.com/pt-BR/square/news/bitcoin%20news'

    noticias = []

    response = requests.get(URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        titulos = soup.find_all('h3', class_='css-yxpvu', limit=10)

        for titulo in titulos:
            noticias.append(titulo.get_text())

        return noticias
    else:
        return 'Algo deu errado durante a requisição para a API de noticias, tente novamente!'
