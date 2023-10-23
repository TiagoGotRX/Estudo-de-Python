Nomes = []
pessos = []
while True:
    Nomes.append(str(input('Nome: ')))
    pessos.append(int(input('Peso: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*40)
print(f'Ao todo, voce cadastrou {len(Nomes)} pessoas')
print(f'O maior peso foi de {max(pessos)} Kg de ',end='')
for c, v in enumerate(pessos):
    if v == max(pessos):
        print(f'{Nomes[c]}',end='')
print(f'\nO menor peso foi de {min(pessos)} de ', end='')
for c, v in enumerate(pessos):
    if v == min(pessos):
        print(f'{Nomes[c]}', end='')
