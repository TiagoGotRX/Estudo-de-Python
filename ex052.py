n = int(input('Digite um numero: '))
tot = 0 
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1 
    else:
        print('\033[31', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[m0 numero {} foi divisivel {} vezes'. format(n, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃo é PRIMO!!!!!')