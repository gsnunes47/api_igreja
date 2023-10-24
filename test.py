import requests

membros = requests.get(url='https://api-igreja.onrender.com/membros')
print(membros)
