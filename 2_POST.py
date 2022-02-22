"""
LINK DA API CRIADO NOS FIREBASE
https://console.firebase.google.com/project/teste-421f4/database/teste-421f4-default-rtdb/data
"""

# * NO 'POST' NAO SE USA A API ...(-MuX4e89WDIChkiMXYsP) E SIM A PADRAO CRIADA NO COMEÇO(https://teste-421f4-default-rtdb.firebaseio.com/)

import requests

# * ENVIA DADO NOVO
# * CRIANDO UMA INFORMAÇÃO DENTRO DO BANCO DE DADOS FEITO NO FIREBASE
# * CRIA UM NOVO ITEM ALEATORIO EX: (-MuX4nTgYGibugcMiBOF)

informacoes = '{"Nome": "Daniel", "sobrenome": "Reinaldo", "Idade": "29"}'
requisicao = requests.post('https://teste-421f4-default-rtdb.firebaseio.com/.json', data=informacoes)

print(requisicao)  # * Response [400, 200]>
print(requisicao.json())


