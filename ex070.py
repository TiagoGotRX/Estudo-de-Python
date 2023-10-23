print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
soma = preço = m = cont = menor = 0
barato = ''
while True:
    prduto = str(input('Nome do Produto: '))
    preço = int(input('Preço: R$'))
    cont += 1
    soma += preço
    if preço >= 1000:
        m += 1     
    if cont == 1 or preço < menor:
        menor = preço
        barato = prduto
    terminar = ' '
    while terminar not in 'SsNn':
        terminar = str(input('Quer continuar? [S/N] ')).upper().split()[0]  
    if terminar in 'Nn':
        print('FIM DO PROGRAMA')
        break
print(f'O total da compra foi {soma}')
print(f'Temos {m} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')