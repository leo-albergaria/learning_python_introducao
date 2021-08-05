# Lembra-se:Número primo é aquele que se divide por 1 e por ele mesmo SOMENTE.
a = int(input('Entre com um número: '))

primo = 0
for counter in range(1, a + 1):
    resto = a % counter
    print(counter, resto)
    if resto == 0:
        primo += 1

if primo == 2:
    print('\nNúmero {} é primo'.format(a))
else:
    print('\nNúmero {} não é primo'.format(a))
