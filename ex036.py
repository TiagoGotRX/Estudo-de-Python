valor = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Em quantos anos vc vai pagar?: '))
prestação = valor / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'. format(valor, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Imprestimo pode ser CONCEDIDO!')
else:
    print('Imprestimo NEGADO!')
