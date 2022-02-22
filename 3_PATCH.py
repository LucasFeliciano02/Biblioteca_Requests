
# * NO PATCH APENAS SE PEGA A API QUE FOI CRIADA PELO POST (-MuX43MXZoX3BvO0hwiM), POIS É UMA EDIÇÃO
# * ENVIA DICIONARIO EDITADO
# * TEM QUE ESPECIFICAR QUEM QUER EDITAR COM BASE NAS INFORMAÇÕES DA BASE DE DADOS
# * PEGAR O LINK DO ITEM  (-MuX43MXZoX3BvO0hwiM) POR EXEMPLO
# * SOBRESCREVER INFORMAÇÕES

import requests

informacoes = '{"Nome": "Draniel"}'
requisicao = requests.patch('https://teste-421f4-default-rtdb.firebaseio.com/-MuX43MXZoX3BvO0hwiM.json', data=informacoes)

print(requisicao)
print(requisicao.json())
