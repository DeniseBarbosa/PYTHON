def soma(x, y):
  return x+y

soma1 =soma(2,5)
soma2 =soma(2,1)
print(soma1+soma2)

def pet(escolher=None):
  if escolher == "x":
    return 'Esse é o meu dog Lui'
  elif escolher == "y":
    return 'Esse é a minha gatinha Pit'
  

retorno = pet()
print(retorno)

