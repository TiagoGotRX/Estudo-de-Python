lanche = ['pao', 'suco', 'pizza', 'pudim',] #Lista
print(lanche[3])
lanche[3] = 'picole'#muda o valor de uma variavel
print(lanche[3])
lanche.append('bolacha') #coloca mais uma variavel a lista
lanche.insert(0, 'cuzcus') #coloca a variavel na possição desejada
print(lanche)
del lanche[3] #apaga a variavel pela chave = 0 1 2 3 
lanche.pop(3) #apaga a variavel pela chave = 0 1 2 3 
lanche.remove('pizza') #apaga a variavel usando o nome/numero dela 
print(lanche)



print('--'*40)
valores = list(range(4, 11)) # cria uma lista em ordem 
numeros = [8,2,5,4,9,3,0] # lista fora de ordem
numeros.sort() #comando sort ordena os valores do menor para o maior
numeros.sort(reverse=True) #comando sort(reverse=True) ordena os valores do maior para o menor
print(valores)
print(numeros)
print(len(numeros)) # Mostra quantos valores tem na lista



print('<->'*15)
print(f'{"AULA PRATICA":^40}')
print('<->'*15)

'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não tem o numero 4 na sua lista')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''




'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):                    #Muito importante
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final')'''



'''a = [2,3,4,7]
b = a[:]     #Ele cria uma ligação mais sim uma cápia
b[2] = 8     #Lista liga uma na outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

