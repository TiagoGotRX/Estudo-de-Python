from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nacs = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - nacs
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))
