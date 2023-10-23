print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
idade = cont = homem = feminino = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    continuar = ' '

    print('-'*20)
    if idade >= 18:
        cont += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff':
        if idade <= 20:
            feminino +=1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).upper().split()[0]
    if continuar in 'N':
        break
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {feminino} mulheres com menos de 20 anos')

