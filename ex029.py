velocidade = float(input('Qual a sua velocidade: '))
multa = (velocidade - 80)* 7
if velocidade <= 80:
    print('Diriga com segurança')
else:
    print('Voce foi multado em {} cuidado'.format(multa))
