from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computqdor "pensar"
print('-=-'* 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em que numero eu pensei ? ')) #jogador tenta adivinhar
print('PROCESANDO...')
sleep(2)
if jogador == computador:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(computador, jogador))