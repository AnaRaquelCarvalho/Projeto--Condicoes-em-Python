print('='*16, 'Radar Eletrônico ','='*16)
velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
print('='*52)

if 80 >= velocidade:
    print('Velocidade Permitida: {} Km/h'.format(80))
    print('Velocidade atual do carro: {} km/km.'.format(velocidade))
    print('Tenha um bom Dia! Dirija com segurança!')
else:
    print('Velocidade atual do carro: {} Km/h'.format(velocidade))
    print('Multado! Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('='*52)
