lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

for x in lista_animal:
    print(x)
print('')

print(sum(lista))
print(min(lista))
print(max(lista))
print('')

if 'gato' in lista_animal:
    print('Existe o gato')
else:
    print('Não existem gato na lista')
if 'Lobo' in lista_animal:
    print('Existe o Lobo')
else:
    print('Não existem Lobo na lista')
print('')

lista_animal.append('Lobo')
if 'Lobo' in lista_animal:
    print('Existe o Lobo')
else:
    print('Não existem Lobo na lista')

lista_animal.pop(1)
if 'gato' in lista_animal:
    print('Existe o gato')
else:
    print('Não existem gato na lista')
print('')

lista_animal.remove('cachorro')
print(lista_animal)
print('')

lista_animal.append('gato')
lista_animal.append('cachorro')
print(lista_animal)
print('')

lista_animal.sort()
print(lista_animal)
print(len(lista_animal))

