expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(') #Coloca um itel na pilha, agora ela é maior que 0
    elif simb == ')':
        if len(pilha) > 0: #Se o cimbolo for ) e plinha for maior que 0,deleta o ultimo itel
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')
 # Resumo do código ele pega todos os (, e depois para cada ) ele deleta um (. casso sobre algum ( sem deleta, ele aponta o erro