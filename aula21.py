'''help(print)
print(input.__doc__)'''




'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem 
    :param: p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='..')
        c += p
    print('FIM!')
    

contador(2, 10, 2)
help(contador)
'''




'''def somar(a=0, b=0, c=0): #parametro opicional
    """
    -> Faz a soma de tres valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 1)'''




'''#ESCOPO DE VARIAVEL

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste< x vale {x}')
#n é uma variavel global e x uma local 

#Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''



'''def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
#print(f'B dentro vale {b}'). daria erro pois não existe fora da estrutura def
#print(f'B dentro vale {c}'). daria erro pois não existe fora da estrutura def'''

'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
#print(f'B dentro vale {b}'). daria erro pois não existe fora da estrutura def
#print(f'B dentro vale {c}'). daria erro pois não existe fora da estrutura def'''

#RETORNO DE VALORES

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2}, {r3}.')'''

#Aula pratica


