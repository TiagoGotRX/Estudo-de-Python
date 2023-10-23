lista = []
lista2 = []
lista3 = []
while True:
    lista.append(int(input('Digiteu um valor: ')))
    con = str(input('Quer continuar? [S/N]'))
    if con in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        lista2.append(c)
    else:
        lista3.append(c)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista2}')
print(f'A lista de impares é {lista3}')