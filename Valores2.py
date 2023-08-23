print('='*12, 'MAIOR E MENOR VALOR - EXEMPLO 2' ,'='*12)
a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
print('='*56)

#Menor Valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Maior Valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('MENOR VALOR: {}'.format(menor))
print('MAIOR VALOR: {}'.format(maior))
print('='*54)