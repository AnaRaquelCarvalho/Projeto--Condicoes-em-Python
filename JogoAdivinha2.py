print('='*16, 'Jogo da Adivinhação 2' , '='*16)
print('[Vou pensar em um número de 0 a 5. Tente adivinhar...]')
print('='*56)
jogador = int(input('Em que número pensei? '))
from random import randint
computador = randint(0,5)

print('    PROCESSANDO...')
#Tempo para processar...
from time import sleep
sleep(3)

if jogador == computador:
    print('Parabéns! Você Venceu! ')
    print("="*60)
else:
    print('Você Errou! Pensei no {} e não no {}!'.format(computador, jogador))
    print('='*16, ' Tente Novamente! ','='*16)