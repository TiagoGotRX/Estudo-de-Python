lista = []

while True:
    n1 = (int(input('Digite um valor: ')))
    if n1 not in lista:
        lista.append(n1)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou considerar...')
    r = str(input('Quer continuar? [S/N]  '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou os valores {lista}')


        
            
