def lin():
    print('-'*30)

'''#Programa principal
lin()
print('Curso em video')
lin()
print('Curso em video')
lin()
print('Curso em video')
lin()'''

'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


#Programa principal
titulo('Curso em video')
titulo('Curso em video')
titulo('Curso em video')'''
'''def titulo():
    print('-'*30)
    print('Aula Pratica')
    print('-'*30)


titulo()

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
print('-='*30)'''


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)
lin()

'''def contador(*num):
    print(num)'''

'''def contador(*num):
    for valor in num:
        print(f' {valor} ',end='')
    print('FIM')'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

contador(2, 1 , 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos += 1

valores = [ 7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)