pessoa = {
  'nome': 'Denise',
  'sobrenome': 'Pereira',
  'idade': 18,
  'altura': 1.8,
  'endereco':[
    {'rua': 'x', 'numero': 123},
    {'cep': 152365, 'estado': 'sp', 'cidade': 'são paulo'},
  ],
}
# print(pessoa['nome'])
objeto ={}
nome = 'mesa'
objeto['cadeira'] = 'de bebe'
objeto[nome] = 'azul'
# alterar o valor 
objeto[nome] = 'preto'
# deletar a chave 
del objeto['cadeira']
print(objeto)
