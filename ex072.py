cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze','Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um nuemro inteiro entre 0 e 20: '))
    if num < 0:
        print('Tente novamente')
    elif num > 20:
        print('Tente novamente')
    else:
        print(f'Voce digitou o numero {cont[num]}')
        res = str(input('Voce quer continuar ? [N/S]: '))
        if res in 'Nn':
            break
        


    



        
