# Utilizando alguns operadores
a = int(input('Entre com o 1° valor: '))
b = int(input('Entre com o 2° valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
# Menos usado
print('Soma: ' + str(soma))

print('Subtração: ' + str(subtracao))
print('Multiplicação: ' + str(multiplicacao))
print('Divisão: ' + str(divisao))
# Mais usado
print('Soma: {} // Subtração: {} // Multiplicação: {} // Divisão: {}'.format(soma, subtracao, multiplicacao, divisao))

print('\nSoma: {} \nSubtração: {} \nMultiplicação: {} \nDivisão: {}'.format(soma, subtracao, multiplicacao, divisao))

print('\nSoma: {A} \nSubtração: {B} \nMultiplicação: {C} \nDivisão: {D}'.format(A=soma,
                                                                                B=subtracao,
                                                                                C=multiplicacao, D=divisao))
resultado = ('\nSoma: {A} \nSubtração: {B} \nMultiplicação: {C} \nDivisão: {D}'.format(A=soma,
                                                                                B=subtracao,
                                                                                C=multiplicacao, D=divisao))

print(resultado)

