print('='*16, 'Custo de uma Viagem' ,'='*16)
distancia = float(input('Qual é a distãncia da viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
    print('Você esta prestes a começar uma viagem de {:.0f} km.'.format(distancia))
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))
else:
    preco = distancia * 0.45
    print('Você esta prestes a começar uma viagem de {:.0f} km.'.format(distancia))
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preco))

print('='*54)
