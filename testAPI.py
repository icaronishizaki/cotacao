from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/moedas', methods=['GET']) 
def get_Moedas():
    msg = "Get Moedas"
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
    msg = "post Dia"
    return msg