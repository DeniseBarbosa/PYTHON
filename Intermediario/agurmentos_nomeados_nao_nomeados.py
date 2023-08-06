'''
Argumento pos
'''

def soma(x, y):
  print(f'{x=} y={y}', '|', 'x + y = ', x + y)
soma(1,2)
soma(x=10, y=50)

'''
definir um valor padrão no parametro
'''
def dados(x, y, padrao=None):
  print(x, y, padrao)
dados(1,2,'casa')