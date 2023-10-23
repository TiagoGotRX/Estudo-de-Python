print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primero termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} _'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA') 
    mais = int(input('Quantos termos vc quer motrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))