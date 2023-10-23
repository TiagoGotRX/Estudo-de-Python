pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'FM' :
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) as mulheres cadastradas foram ', end='')
for l in galera:
    if l['sexo'] in 'Ff':
        print(f' {l["nome"]} ', end='')
print()
print(f'D) Kista das pessoas que estão acima da média: ', end='')
for l in galera:
    if l['idade'] >= média:
        print('   ')
        for k, v in l.items():
            print(f' {k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
