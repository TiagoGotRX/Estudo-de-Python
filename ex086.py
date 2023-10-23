'''valor = 0
n = []
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    n.append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    n.append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    n.append(valor)
print('-='*40)
print(f'[ {n[0]} ]  [ {n[1]} ]  [ {n[2]} ]  \n[ {n[3]} ]  [ {n[4]} ]  [ {n[5]} ]  \n[ {n[6]} ]  [ {n[7]} ]  [ {n[8]} ] ] ') '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()