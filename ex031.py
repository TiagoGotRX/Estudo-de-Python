Km = float(input('Quantos kilometros sua viagem tem: '))
print('Voce está preste a começar uma viagem de {}Km.'.format(Km))
if Km <= 200:
    preço = Km * 0.50
else:
    preço = Km * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))