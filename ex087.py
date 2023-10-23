matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna = 0
mai = pares = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            coluna += matriz[l][c]
        if matriz[l][c] == matriz[1][c]:
            mai.append(matriz[l][c])
    print()
print('-='*30)
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {max(mai)} e o menor é {min(mai)} ')
