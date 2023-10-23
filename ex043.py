peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÈNS voce esta na faixa de PESO NORMAL')
elif 25 <= imc <30:
    print('Voce está em SPBREPESO')
elif 30 <= imc < 40:
    print('Voce está em OBESIDADE, Cuicado!')
elif imc >= 40:
    print('Voce está em OBESIDADE MÓRBIDA, cuidado!')