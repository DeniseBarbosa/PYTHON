import copy
produtos = [
  {'nome': 'leite', 'preco': 4.49},
  {'nome': 'cafe', 'preco': 5.00},
  {'nome': 'feijão', 'preco': 8.75},
  {'nome': 'açucar', 'preco': 2.96},
  {'nome': 'macarrão', 'preco': 11.12},
  {'nome': 'arroz', 'preco': 6.32},
  {'nome': 'pimentão', 'preco': 8.65},
  {'nome': 'azeite', 'preco': 1.92},
]
# fazendo uma copia dos produtos original 
copia_produtos = copy.deepcopy(produtos)
# subir os preços de todos os produtos para 10% 
'''
aqui eu não estou alterando o produto final, apenas fazendo
uma copia com os preços alterados para 10%
'''
copia_produtos = [ {**p, 'preco': round(p['preco']*1.1, 2)}
                  for p in produtos
                  ]
# ordenar os produtos do maior para o menor (nome)
ordenar_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    # reverse=True
)

#ordernar do maior para o menor preço
ordenar_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
   
)

# somar todos os valores da lista
lista_somada = round(sum(p['preco'] for p in copia_produtos), 2)

print(lista_somada)

# obter uma lista que contenha os preços somados
lista_precos_somados = [p['preco'] for p in copia_produtos]

print(lista_precos_somados)

# print(*copia_produtos, sep='\n')
# print()
# print(*ordenar_nome, sep='\n')
# print()
# print(*ordenar_preco, sep='\n')

