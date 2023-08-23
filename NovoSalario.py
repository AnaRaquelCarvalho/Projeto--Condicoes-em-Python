print('='*16, 'Novo aumento de Salário' ,'='*16)
nome = str(input('Nome Completo: '))
salario = float(input('Salário R$ '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} .AGORA.'.format(salario, aumento))

print('='*58)