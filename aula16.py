'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(lanche[cont])
for comida in lanche:
    print(f'Eu vo comer {comida}')'''



lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')



'''a = (8, 0, 4, 1,) #tupla a
b = (1, 5, 6, 9,)#tupla b
c = b + a #Junta as 2 tuplas em uma, levando em consideração, O primeiro a ser somado isso definira a forma da tupla
print(c)
print(c.index(5, 1)) #Mostra em qual possisão aprarece o numero pela primeira vez
print(c.count(5)) #conta quatos do numero tem na tupla

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #deleta a tupla inteira
print(pessoa)'''
