dados = {}
import datetime
dia_atual = datetime.date.today().year
for c in range(1):
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Ano de Nascimento: '))
    dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['carteira'] == 0:
        break
    dados['contrato'] = int(input('Ano de Contratação: '))
    dados['salario'] = int(input('Salário: R$'))
print('-=' * 30)
print(f'  - nome tem o valor {dados["nome"]}')
print(f'  - idade tem o valor {dados["idade"]}')
print(f'  - carteira tem o valor {dados["carteira"]}')
if dados['carteira'] != 0:
    print(f'  - contratação tem o valor {dados["contrato"]}')
    print(f'  - salário tem o valor {dados["salario"]}')
    valor =  dia_atual -  dados['idade']
    print(f'  - aposentadoria tem o valor {((dados["contrato"] - dia_atual) + 35) + valor}')
    