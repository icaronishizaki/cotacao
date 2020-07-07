import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import conexao_mongo

cotacao = {
    "Dolar": "https://dolarhoje.com/",
    "Libra": "https://dolarhoje.com/libra-hoje/",
    "Euro": "https://dolarhoje.com/euro-hoje/",
    "Ouro": "https://dolarhoje.com/ouro-hoje/",
    "Bitcoin": "https://dolarhoje.com/bitcoin-hoje/"
}

def start():

    for key, value in cotacao.items():

        r = requests.get(value)

        soup = BeautifulSoup(r.content, 'html5lib') 

        value_estrangeira = soup.find('input', attrs = {'id':'nacional'}).get_attribute_list('value')[0]

        data = datetime.now()

        conexao_mongo.save(key, { "value": value_estrangeira, "date": str(data) })
