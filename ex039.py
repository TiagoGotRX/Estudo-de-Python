from datetime import date
print('''Nos informe o seu sexo:
[1] Feminino
[2] Masculino''')
sexo = int(input(' '))
atual = date.today().year
nasc = int(input('Ano de nacimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 1:
    print('Voce não é obrigada a se alistar')
elif idade == 18:
    print('Voce tem q alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamente'.format(saldo))
    ano = atual = saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif sexo == 1:
    print('Voce não é obrigada a se alistar')