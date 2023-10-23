'''valores = []
mai = men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('=-'*30)
print(f'Voce digitou os valores {valores}')

print(f'O maior valor digitado foi {mai} nas posições ',end=' ')
for i, l in enumerate(valores):
    if l == mai:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {men} nas posições',end=' ')
for i, l in enumerate(valores):
    if l == men:
        print(f'{i}...',end='')'''


valores = []
mai = men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*30)
print(f'Voce digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ',end=' ')
for i, l in enumerate(valores):
    if l == max(valores):
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições',end=' ')
for i, l in enumerate(valores):
    if l == min(valores):
        print(f'{i}...',end='')








