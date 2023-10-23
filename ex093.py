lista = {}
partidas = []
lista['nome'] = str(input('Nome do Jogador: '))
cont = int(input(f'Quantas partidas o {lista["nome"]} jogou? '))
for c in range(0, cont):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
lista['gols'] = partidas[:]
lista['total'] = sum(partidas)
print('-='*30)
print(f'{lista}')
print('-='*30)
for c, p in lista.items():
    print(f'O campo {c} tem o valor {p}')
print('-='*30)
print(f'O jogador {lista["nome"]} jogou {cont} partidas.') 
for c in range(cont):
    print(f'   => Na partida {c}, fez {lista["gols"][c]} gols.')
print(f'Foi um total de {lista["total"]} gols.')
