from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
cont = n = soma = computador = 0
while True:
    computador = randint(0, 10)
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper()
    soma = n + computador
    if escolha in 'Pp':
        if soma % 2 == 0:
            cont += 1
            print('=-'*20)
            print(f'Voce jogou {n} e o computador {computador}. total de {soma} DEU PAR ')
            print('=-'*20)
            print('-='*25)
            print('VOCE VENCEU !')
            print('-='*25)
        if soma % 2 != 0:
            print('-'*60)
            print(f'Voce jogou {n} e o computador {computador}. total de {soma} DEU IMAPAR ')
            print('-'*60)
            print('VOCE PERDEU!')
            print('-='*25)
            print(f'GAME OVER! VOCE VENCEU {cont} VEZES.')
            break
    if escolha in 'Ii':
        if soma % 2 != 0:
            cont += 1
            print('-'*60)
            print(f'Voce jogou {n} e o computador {computador}. total de {soma} DEU IMPAR ')
            print('-'*60)
            print('VOCE VENCEU !')
            print('-='*25)
        if soma % 2 == 0:
            print('-'*60)
            print(f'Voce jogou {n} e o computador {computador}. total de {soma} DEU PAR ')
            print('-'*60)
            print('VOCE PERDEU!')
            print('-='*25)
            print(f'GAME OVER! VOCE VENCEU {cont} VEZES.')
            break


