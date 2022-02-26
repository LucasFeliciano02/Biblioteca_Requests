"""
- LINK API FEITO NO REPLIT utlizando bd do excel =  https://replit.com/@LucasFeliciano0/MinhaAPI#main.py

REPLIT NAO DEIXA O SERVIDOR O TEMPO TODO NO AR CASO NAO PAGAR
LOGO, VAR UM PROCESSO DE DEPLOY DESSE CODIGO PRA UM SERVIDOR OFFICIAL COMO DO HEROKU (GRAÇA), PARA API POUCO UTILIZADA

- O DEPLOY DE UMA API É O MESMO PROCESSO QUE SE FAZ AO CONSTRUIR UM SITE

"""
# * PEGANDO INFORMAÇÃO DA API FEITA NO SITE REPLIT.COM  (GET PADRAO)

import requests

link = 'https://MinhaAPI.lucasfeliciano0.repl.co/pegar_vendas'

# dicionario esta usando essa requisicao:  dicionario = requisicao.json()
requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())  # FORMATO {'total_vendas': 3026.1000000000004}


dicionario = requisicao.json()

vendas = dicionario['total_vendas']

print(f'total de vendas ${vendas}')
