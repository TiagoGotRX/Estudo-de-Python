listaNomes = []
listaPesos = []

while True:
    nome = str(input('Nome: '))
    listaNomes.append(nome)
    peso = float(input('Peso (kg): '))
    listaPesos.append(peso)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('_' * 40)
print(f'Ao todo, você cadastrou {len(listaNomes)} pessoas')
print(f'O(s) maior(es) peso(s) foi de {max(listaPesos)} kg de ', end='')
for c, v in enumerate(listaPesos):
    if v == max(listaPesos):
        print(f'{listaNomes[c]}, ', end='')
print(f'\nO(s) menor(es) peso(s) foi de {min(listaPesos)} kg de ', end='')
for c, v in enumerate(listaPesos):
    if v == min(listaPesos):
        print(f'{listaNomes[c]}, ', end='')
print()