# declarando uma função
def funcao(a, b, c):
  print(a, b, c)
# argumento
funcao('arvore', 'boca', 'casa')
# é possivel colocar outros valores diferentes nos parametros(na mesa função que representado nesse exemplo)
funcao('rua', 2023, 'pipoca')

# Vamos para outro exemplo 
def saudacao(nome):
  print(f'Olá {nome}')

saudacao('Denise')
saudacao('Pedro')
saudacao('Maria')
'''
Se caso voce chamar a função e não passar um argumento, podemos definir um valor default (padrão)
segue o exemplo abaixo
'''
def pet(nome='dog'):
  print(f'Esse é o meu -> {nome}')
pet('Gatinho')
pet()

def multiplo_de(numero, multiplo):
        resultado = numero % multiplo == 0
        print(f'{numero} é múltiplo de {multiplo}?', end=' ')
        print(resultado)
     
     
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)