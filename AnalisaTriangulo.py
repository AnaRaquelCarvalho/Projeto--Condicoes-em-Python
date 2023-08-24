print('='*16, 'Analisador de Triãngulos' ,'='*16)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PODEM FORMAR UM TRIÂNGULO: ')
else:
    print('NÃO PODEM formar um triângulo: ')

print('=' * 46)