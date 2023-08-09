import requests

url = 'http://localhost:8000/'
resposta = requests.get(url)
print(resposta.text)