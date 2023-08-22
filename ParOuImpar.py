print('='*16, 'Par ou Ímpar ','='*16)
n = int(input('Digite um número: '))
n1 = n % 2
if n1 == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))
print('='*46)