somaidade = 0
mediaidade = 0
meioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sex0 [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        meioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > meioridadehomem:
        meioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(meioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))