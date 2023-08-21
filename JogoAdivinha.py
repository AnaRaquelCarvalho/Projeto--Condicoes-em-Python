print('='*18, 'Jogo da Adivinhação' ,'='*18)
print('[Vou pensar em um número de 0 a 5. Tente adivinhar...]')
print('='*56)
import random
jog = int(input('Em que número pensei? '))
comput = random.randint(1,5)

#Tempo para o computador pensar...7
from time import sleep 
print('    Processando...')
sleep(2)
if jog == comput:
    print('Parabéns! O número é {}'.format(jog,comput))
    print('='*56)
else:
    print('Você Errou! Eu pensei no {} e não no {}!'.format(comput,jog))   
    print('='*16, 'Tente Novamente!!!! ', '='*16,'\n')

    
     


