print('='*16, 'Radar Eletrônico ','='*16)
velocidade = float(input('Qual a velocidade atual do carro? '))
print('='*52)

if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(multa))

print('Tenha um bom Dia! Dirija com segurança!')
print('='*52)