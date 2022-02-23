
# * ENTRAR NO LINK DO ITEM QUE QUER DELETAR

import requests

requisicao = requests.delete('https://teste-421f4-default-rtdb.firebaseio.com/-MuX4e89WDIChkiMXYsP.json')

print(requisicao)  
print(requisicao.json())