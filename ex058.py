from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi ? ')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou = True
    elif jogador >= computador:
        print('Um pouco menos')
    elif jogador <= computador:
        print('Um pouco mais')
    tentativas += 1
print('Acertou! vc tentou {} vezes!'.format(tentativas))

