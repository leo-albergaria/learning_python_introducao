# Digitar as notas para mensuração.
a = int(input('Entre com a nota do 1° bimestre: '))
while a > 10:
    a = int(input('Nota deverá ser menor ou igual a 10. Entre com a nota do 1° bimestre: '))

b = int(input('Entre com a nota do 2° bimestre: '))
while b > 10:
    b = int(input('Nota deverá ser menor ou igual a 10. Entre com a nota do 2° bimestre: '))

c = int(input('Entre com a nota do 3° bimestre: '))
while c > 10:
    c = int(input('Nota deverá ser menor ou igual a 10. Entre com a nota do 3° bimestre: '))

d = int(input('Entre com a nota do 4° bimestre: '))
while d > 10:
    d = int(input('Nota deverá ser menor ou igual a 10. Entre com a nota do 4° bimestre: '))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
else:
    print('Foi informado alguma nota errada.')
