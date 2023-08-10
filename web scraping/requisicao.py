import requests
from bs4 import BeautifulSoup
url = 'http://localhost:8000/'
resposta = requests.get(url)
html = resposta.text
analisando_html = BeautifulSoup(html, 'html.parser')
print(analisando_html.title)
print(analisando_html.title.text)
selecionar = analisando_html.select_one('#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')
print(selecionar.text)
print("------------------------------------------------------------------------------------------------------------------------------")
artigo = selecionar.parent
print(artigo)
print("------------------------------------------------------------------------------------------------------------------------------")
paragrafos = artigo.select('p')
print(paragrafos)
print("------------------------------------------------------------------------------------------------------------------------------")
if artigo is not None:
    for p in artigo.select('p'):
        print(p)