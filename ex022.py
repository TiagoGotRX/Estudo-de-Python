nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome maiusculas é {}'.format(nome.upper()))
print('Seu nome minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letrs'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} lestras'.format(separa[0],len(separa[0])))