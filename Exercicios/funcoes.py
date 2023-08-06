def multiplicar(*args):
  total = 1
  for numero in args:
    total = total * numero
  return total
multiplicacao = multiplicar(1,2,3)
print(multiplicacao)

'''
verificar se o numero é par ou impa
'''
def par_impa(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impa(3))
