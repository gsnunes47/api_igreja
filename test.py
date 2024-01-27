import requests

membros = requests.post(url='https://api-igreja.onrender.com/membros', json='')
membros = requests.get(url='https://api-igreja.onrender.com/membros')
print(membros)
