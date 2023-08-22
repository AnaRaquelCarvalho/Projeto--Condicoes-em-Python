print('='*8, 'Analisando se o ano é Bissexto ou não' ,'='*8)
ano = int(input('Coloque o ano que deseja verificar: '))

from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXT0.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))
 
 