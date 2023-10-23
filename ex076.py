lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90 )
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-'*40)





























'''print('-'*40)
print('          LISTAGEM DE PREÇOS')
print('-'*40)
print(f'{lista[0]}.................R$  {lista[1]}')
print(f'{lista[2]}.................R$  {lista[3]}')
print(f'{lista[4]}.................R$  {lista[5]}')
print(f'{lista[6]}.................R$  {lista[7]}')
print(f'{lista[8]}.................R$  {lista[9]}')
print(f'{lista[10]}.................R$  {lista[11]}')
print(f'{lista[12]}.................R$  {lista[13]}')
print(f'{lista[14]}.................R$  {lista[15]}')
print(f'{lista[16]}.................R$  {lista[17]}')'''


   

'''for itens, pos in enumerate(lista):
    print(f'{pos[0]}.................R$  {pos[1]}')'''