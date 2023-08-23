print('='*16, 'Aumento de Salário' ,'='*16)
nome = str(input('Nome Completo: '))
salario = float(input('Salário R$ '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} .AGORA.'.format(salario, aumento))
else:
    aumento1 = salario + (salario * 15 / 100)
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} .AGORA.'.format(salario, aumento1))

print('='*54)