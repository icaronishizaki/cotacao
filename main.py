from flask import Flask, request, jsonify
import conexao_mongo
import bot_cotacao

#API
app = Flask(__name__)

@app.route('/moedas', methods=['GET']) 
def get_Moedas():
    msg =  conexao_mongo.collection
    return msg

@app.route('/moedas', methods=['POST']) 
def post_Moedas():
    msg = "Post Moedas"
    return msg
    
@app.route('/dia', methods=['GET']) 
def get_Dia():
    msg = "Get Dia"
    return msg

@app.route('/dia', methods=['POST']) 
def post_Dia():
    bot_cotacao.start()
    msg = "Moedas Atualizadas"
    return msg