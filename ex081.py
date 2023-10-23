'''lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    po = str(input('Quer continuar? [S/N]'))
    if po in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são {lista}')
for c in lista:
    if c == 5:
        cont += 1
if cont >= 1:
    print('O valor 5 foi encotrado na lista!')

elif cont == 0:
    print('O valor 5 não foi encontrado na lista!')'''
        
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    po = str(input('Quer continuar? [S/N]'))
    if po in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')