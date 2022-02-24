
# * https://replit.com/@LucasFeliciano0/MinhaAPI#main.py  =  codigos estao aqui, nao funcionara no vscode pois la se importa um arquivo excel
# api criada usando o Flask no site replit

# REPLIT.COM

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# AQUI SE CONSTROI AS FUNCIONALIDADES

# Para pagina do site em construção, tem que definir um função e a mesma estrutura sera usada por uma api
# VC constroi uma função em que vc retorna qual informação vc quer que apareça na pagina do seu site
# Pra cada função dessa que vai ser uma página, vc tem que atribuir um link pra essa função com o decorator:    @app.route(), que diz em qual link vai rodar essapagina  ('/')  = pg padrao


@app.route('/')
def homepage():
    return 'A API Está no ar'


# api vai calcular o total de vendas
@app.route('/pegar_vendas')
def pegar_vendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')  # colocar o nome do arquivo que queres pegar as informações
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


# RODANDO NOSSA API

# instataneamente esta disponivel para qualquer pessoa do mundo e gero um link que faz isso, aparece do lado como se fosse o proprio site web

app.run(host='0.0.0.0')

# tabela = pd.read_csv('12-18 - Criando API no Python.csv')
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)
