print('='*23, 'Radar Eletrônico ','='*23)
from random import randint
velocidade = randint(0,200)
velocidadeMax = velocidade - 80
multa = velocidadeMax * 7

if 80 >= velocidade:
    print('Velocidade Permitida: {} Km/h'.format(80))
    print('Velocidade do carro: {} km/km.'.format(velocidade))
    print('Tenha um bom Dia! Dirija com segurança!')
else:
    print('Velocidade do carro: {} Km/h'.format(velocidade))
    print('Multado! Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))
print('='*66)
