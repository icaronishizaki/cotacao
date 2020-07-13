import json
from collections import namedtuple


def _object_hook(converted_dict):
    return namedtuple('X', converted_dict.keys())(*converted_dict.values())


def json_to_obj(data):
    return json.loads(data, object_hook=_object_hook)


def cotacoes():
    return {
        "Dolar": "https://dolarhoje.com/",
        "Libra": "https://dolarhoje.com/libra-hoje/",
        "Euro": "https://dolarhoje.com/euro-hoje/",
        "Ouro": "https://dolarhoje.com/ouro-hoje/",
        "Bitcoin": "https://dolarhoje.com/bitcoin-hoje/"
    }
