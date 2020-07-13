from datetime import datetime
from flask import Flask, request, Response
import mongo
import bot_cotacao
from helpers import json_to_obj, cotacoes

# API
app = Flask(__name__)


@app.route('/moedas', methods=['GET'])
def get_moedas():
    msg = mongo.collection
    return msg


@app.route('/dia', methods=['GET'])
def get_dia():
    msg = "Get Dia"
    return msg


@app.route('/dia', methods=['POST'])
def post_dia():
    if 'acao' in request.headers:
        acao = request.headers['acao']
        if acao == 'coleta-diaria':
            bot_cotacao.start()
            return Response(status=202)
    if request.data == b'':
        return Response('bad request', status=400)
    else:
        body = json_to_obj(request.data)
        if hasattr(body, 'payload'):
            payload = json_to_obj(body.payload)
            if hasattr(payload, 'moeda') and hasattr(payload, 'valor'):
                for key, value in cotacoes().items():
                    if str(payload.moeda).capitalize() == key:
                        mongo.save(key,
                                   {
                                       "value": payload.valor,
                                       "date": str(datetime.now())
                                   })
                        return Response('ok', status=201)
    return Response('bad request', status=400)
