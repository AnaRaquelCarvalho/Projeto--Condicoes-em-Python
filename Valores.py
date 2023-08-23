print('='*16, 'Maior e Menor valor' ,'='*16)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
print('='*54)

# Menor valor digitado
if n1 < n2 and n1 < n3:
    print('O MENOR VALOR digitado foi {}'.format(n1))
if n2 < n3:
    print('O MENOR VALOR  digitado foi {}'.format(n2))
else:
    print('O MENOR VALOR digitado foi {}'.format(n3))

# Maior valor digitado
if n1 > n2 and n1 > n3:
    print('O MAIOR VALOR digitado foi {}'.format(n1))
if n2 > n3:
        print('O MAIOR VALOR  digitado foi {}'.format(n2))
else:
    print('O MAIOR VALOR digitado foi {}'.format(n3))
print('='*54)    