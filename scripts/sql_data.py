import sqlite3
from .api_data import data_info 

banco = sqlite3.connect('/home/guilherme/Projetos/cripto/cripto_data.db')

cursor = banco.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS criptomoedas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    preco REAL NOT NULL,
    data TEXT NOT NULL
)
''')

banco.commit()

def salva_dados_banco(dados):
    cursor.execute(f'''
    INSERT INTO criptomoedas (preco, data) VALUES (?, ?)
    ''', (dados[0], dados[1]))
    banco.commit()

def busca_dados_banco():
    cursor.execute('SELECT * FROM criptomoedas')
    rows = cursor.fetchall()

    resultados = []

    for row in rows:
        id, preco, data = row
        resultados.append((id, preco, data))

    return resultados
