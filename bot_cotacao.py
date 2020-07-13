import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mongo
import helpers


def start():
    for key, value in helpers.cotacoes().items():
        r = requests.get(value)
        soup = BeautifulSoup(r.content, 'html5lib')
        value_estrangeira = soup.find('input', attrs={'id': 'nacional'}).get_attribute_list('value')[0]
        data = datetime.now()
        mongo.save(key, {"value": float(value_estrangeira.replace(',', '.')), "date": str(data)})
