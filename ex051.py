primeira = int(input('Primeira termo: '))
razão = int(input('Razão: '))
decimo = primeira + (10 - 1)* razão
for c in range(primeira, decimo, razão):
    print('{} '.format(c), end='-')
print('Acabou')