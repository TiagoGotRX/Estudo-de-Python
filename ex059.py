from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor : '))
opção = 0
while opção != 5:
    print('-=-'* 7)
    print('''     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior
     [ 4 ] novos números
     [ 5 ] sair do programa''')
    print('-=-'* 7)
    escolha = int(input('Qual é sua opção: '))
    print('-=-'* 7)
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    if escolha == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    if escolha == 3:
        if n1 >= n2:
            print('o maior numero é {}'.format(n1))
        if n2 >= n1:
            print('O maior numero é {}'.format(n2))
    if escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor : ')) 
    if escolha == 5:
        sleep(2)
        print('Adeus')
        opção = 5
    if escolha > 5:
        print('opção invalida. Tente novamente!')
