lista = []
vezes = soma = aluno = 0
while True:
    nome = str(input('Nome: '))
    Nota1 = float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    lista.append([nome, Nota1, Nota2])
    cont = str(input('Quer continuar? [S/N] '))
    vezes += 1
    if cont in 'Nn':
        break
print('-='*50)
print('No.   NOME         MÉDIA')
print('-'*35)
for l in range(0, vezes):
    soma = (lista[l][1] + lista[l][2]) / 2
    print(f'{l:^3}   {lista[l][0]:^6}         {soma}')
print('-='*25)
while True: 
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZADO...')
        print(f'{"VOLTE SEMPRE":^30}')
        break
    print(f'Notas de {lista[aluno][0]} são {lista[aluno][ 1: ]} ')
    print('-'*40)
    



