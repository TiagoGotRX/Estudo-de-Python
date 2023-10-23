from random import sample
from time import sleep
lista = sorteados = []
quant = 0
print('-'*50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-'*50)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'{F"SORTEANDO {quant} JOGOS":^50}')
for c in range(1, 60+1):
    lista.append(c)
for c in range(1, quant+1):
    sorteados = sample(lista, 6)
    print(f'Jogo {c}: {sorteados}')
    sleep(1)
print(f'{"< BOA SORTE! >":^50}')

