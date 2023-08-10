# Basic Syntax roadmap 
# append adicional no final da lista 
# pop() remove no final da lista 
lista=[]
lista.append(1) 
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(3400)
lista.append('ursinho')
# lista.pop() 
# print(lista)
# print(lista[-1])
# print(lista[10])
lista_obj = ['cama','brinquedo','carro','fone de ouvido','camisa','casa']
lista_obj.append('copo')
print(lista_obj)
print(lista_obj[1:3])
print(lista_obj[3:])
print(lista_obj[:: 3])
print(lista_obj[:: -1])
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
# Faça uma cópia profunda de uma camada usando fatias 
lista_objeto = lista_obj[:]
del lista_objeto [3]
print(lista_objeto)
# Insere um elemento em um índice específico 
lista_objeto.insert(2, 'computador')
print(lista_objeto)
# Obtém o índice do primeiro item encontrado correspondente ao argumento 
print(lista_objeto.index("computador"))
lista_numeros = [1,2,3]
duas_listas = lista_numeros + lista_objeto
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
print(duas_listas)
# Concatena listas com "extend()" 
lista_cores = ['azul','preto','roxo']
lista_cores.extend(duas_listas)
print(lista_cores)
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
# Verifica a existência em uma lista com "in" 
existe = 'verde' in lista_cores
print(existe)
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
# Você pode desempacotar tuplas (ou listas) em variáveis 
pizza, parque, cinema =  ('refrigerante', 'sol', 'pipoca')
print(pizza)
print("-----------------------------------------------------------------------")
print("-----------------------------------------------------------------------")
# Aqui está um dicionário pré-preenchido 
dicionario = {"cor": "azul", "numero":123, "temPet": False}
# Obtenha todas as chaves como um iterável com "keys()". Precisamos envolver a chamada em list() 
print(list(dicionario.keys()))
# Obtenha todos os valores como um iterável com "values()". Mais uma vez, precisamos envolvê-lo 
# em list() para tirá-lo do iterável. Observação - Igual ao acima em relação à 
# ordenação da chave 
print(list(dicionario.values()))
# Verifique a existência de chaves em um dicionário com "in" 
existe_dic = "temPet" in dicionario

print(existe_dic)
print(dicionario.get("um"))
print(dicionario.get("numero"))
# inseri chave e valor em um dicionario apenas se a chave nao existir 
print(dicionario.setdefault("passeio", "parque"))
print(dicionario.setdefault("endereco", 2))
print(dicionario.setdefault("temPlanta", True))
# Atualizar o dicionario  e adicionar se vc colocar a chave como cores: blue ele vai adcionar no final do dicionario
print(dicionario.update({"cor": "rosa"}))
# Remova as chaves de um dicionário com del 
del dicionario ["endereco"]
print(dicionario)
print("------------------------------------------------------------------")
# ################################################### ## 
# ## 3. Fluxo de controle e iteráveis 
# ​​######################################################
# Percorra uma lista para recuperar o índice e o valor de cada item da lista: 
animals  =  [ "dog" ,  "cat" ,  "mouse" ] 
for  index ,  valor  in  enumerate ( animals ): 
    print(  index, valor )












