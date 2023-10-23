numero = int(input('Digite um numero inteiro')) 
resultado = numero % 2 
if resultado == 0:
    print('O Resultado {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))