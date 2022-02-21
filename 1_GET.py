"""
LINK DA API CRIADO NOS FIREBASE
https://console.firebase.google.com/project/teste-421f4/database/teste-421f4-default-rtdb/data
"""

# * USANDO FIREBASE PARA RECEBER INFORMAÇÕES

import requests  # importar a biblioteca primeiro

requisicao = requests.get('https://teste-421f4-default-rtdb.firebaseio.com/.json')
print(requisicao)  # * Response [400, 200]>
print(requisicao.json())
