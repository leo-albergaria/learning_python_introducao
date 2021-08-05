# Algumas condições - Lembra-se: No python é importante a identação.
a = int(input('Entre com o 1° valor: '))
b = int(input('Entre com o 2° valor: '))
c = int(input('Entre com o 3° valor: '))
print('')
if a > b:
    print('O maior número é {} '.format(a))
else:
    print('O maior número é {} '.format(b))
print('')
if a > b and a > c:
    print('O maior número é {} '.format(a))
elif b > a and b > c:
    print('O maior número é {} '.format(b))
else:
    print('O maior número é {} '.format(c))
print('')

resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0:
    print('Foi digitado um número par.')
else:
    print('Não foi digitado número par.')

print('\nFinal do programa')

