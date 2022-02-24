
# * https://replit.com/@LucasFeliciano0/MinhaAPI#main.py

import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def homepage():
    return 'A API Está no ar'


# api vai calcular o total de vendas
@app.route('/pegar_vendas')
def pegar_vendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')  
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


app.run(host='0.0.0.0')
