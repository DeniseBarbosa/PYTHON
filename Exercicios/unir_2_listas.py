from itertools import zip_longest

# Vamos combinar as listas
lista1=['pizza combina com', 'pop combina com', 'azul combina com', 'cinema combina com']

lista2=['refrigerante', 'dança', 'amarelo']
resultado = list(zip(lista1, lista2))
resultado2 = list(zip_longest(lista1,lista2, fillvalue='pipoca'))

print(resultado)
print()
print(resultado2)