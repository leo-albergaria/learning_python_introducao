b = int(input('Entre com um 1° valor da Faixa de Busca: '))
a = int(input('Entre com um 2° valor da Faixa de Busca: '))

for num in range(b, a + 1):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(num)
