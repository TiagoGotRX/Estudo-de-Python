n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
nota = ( n1 + n2)/ 2
if nota < 5:
    print('A média do aluno foi {} e está reprovado'.format(nota))
elif nota <= 6.9:
    print('A media do aluno foi {} e está de recuperação'.format(nota))
elif nota >= 7:
    print('A média do aluno foi {} e está aprovado'.format(nota))
