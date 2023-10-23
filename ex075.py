'''n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))
n5 = (n1, n2, n3, n4)
tup = ()
print(f'Voce digitou os valores {n5}')
print(f'O valor 9 apareceu {n5.count(9)} vezes')
if 3 in n5:
    print(f'O valor 3 apareceu na {n5.count(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
for numero, pos in enumerate(n5):
    if pos % 2 == 0:
        tup += (pos,)
print(f'Os valores pares digitados foram {tup} ')'''

num = (int(input('Digite um valor: ')),
      int(input('Digite outro valor: ')),
      int(input('Digite mais um valor: ')),
      int(input('Digite o ultimo valor: '))) 
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end="")