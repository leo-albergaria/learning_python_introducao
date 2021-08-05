# Digitar as notas para mensuração.
a = int(input('Entre com a nota do 1° bimestre: '))
b = int(input('Entre com a nota do 2° bimestre: '))
c = int(input('Entre com a nota do 3° bimestre: '))
d = int(input('Entre com a nota do 4° bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
else:
    print('Foi informado alguma nota errada.')
