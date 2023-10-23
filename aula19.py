filme = {'titulo':'Star Wars',
'ano':1977,
'diretor':'George Lucas'
}
print(filme.values()) #Retorna todo os valores
print(filme.keys()) #Pegas todas as cheves 
print(filme.items()) #Pega todos os valores do dicionário

# exemplo de aplicação no for
'''for k, v in filme.items():
    print(f'O {k} é {v}')'''

#ATENÇÃO NISSO!!!. VC PODE COLOCAR DICIONARIO DETRO DE LISTAS


print('AULA PRATICA')

'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f' o {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas ['peso'] = 98.5
pessoas['nome'] = 'leandro'
del pessoas['sexo']
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f' {k} = {v}')'''


'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ,'}
estado2 = {'if': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla '])'''

'''estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federatica: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''
