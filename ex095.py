time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear #Limpa o dicionário jogador, para q possa ser cadastrado outro jogador, caso comtrario não sera adicionado outro jogador
    jogador['nome'] = str(input('Nome do jogador: '))#Recebe um input q pergunta o nome do jogador. Pega esse nome e joga dentro do dicionário jogador['nome']
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()#Limpa a lista de partidas, caso contrário a lista no jogado passado será acresentada na do proximo jogador
    for c in range(0, tot):#Esse for é para receber os gols de cada partida
        partidas.append(int(input(f'   Quantos gols na partida {c+1}?  ')))
    jogador['gols'] = partidas[:]#Pega uma cópia dos gols da lista de partidas e joga dentro do dicionário jogador['gols']
    jogador['total'] = sum(partidas)# Soma o resultados da lista de partidas e joga dentro do dicionário jogado['total']
    time.append(jogador.copy())#Pega todo o dicionário jogador['gols']['total']["nome"] e coloca uma cópia dentro da lista = time, assim guardando os dados de cada jogador individualmente, podendo ser acessado por indice posteriormente
    while True: # Validação de resposta
        resp = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':#Finalização da lista de jogadores
        break
print('-='*30)
for i in jogador.keys():#Pega as chaves do dicionário jogador. i = 0[nome] 1[gols] 2[total]
    print(f'{    i:<15}', end='')#{i:<15} Serve para dar 15 de espaçamento de cada chave. end='' Serve apenas para não quebrar a linha
print()#Serve apenas para quebrar a linha quando o for acabar. 
#Resultado disso.   nome           gols           total
print('-'*40)
for k, v in enumerate(time):#enumerate(time) = k(indice). v(lista(time)). serve para mostra por ordem de cadastra
    print(f'{k:>4}', end='')#Mostra o indice que siginifica a possisão do jogador no cadastro
    for d in v.values():#v.values = (os valores do jogador como [nome] [gols] [total]). d = indice = 0[nome], 1[gols], 2[total]. (Sendo os sados do jogador do indice (k))
        print(f'{str(d):<15}',end='')#Mostra os dados do jogador. d = 0[nome], 1[gols], 2[total]. com 20 de espaçamento
    print()#quebra de linha
print('-'*40)
while True:#Estrutura para mostrar dados do jogador escolhido pela variavel (Busca)
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))#Variavel busca, pegunta o ince do jogador na lista (time), para mostrar seus dados
    if busca == 999:#casso a variavel busca for = (999). o programa se encerra
        break#para o programa 
    if busca >= len(time):#Analisa a varivel busca para ver o indice do jogador esculhino. caso não tenho o indice digitado aparecerá uma mensagem de erro e pedira para digitar novemente 
        print(f'ERRO! Não existe jogador com codigo {busca}! ')#Mensagem de ERRO!
    else:#Se tudo estiver correto, aparecerá as informações a baixo
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')#Mostra o nome do jogador que será feito o levantamento
        for i, g in enumerate(time[busca]["gols"]):#time[busca]["gols"] = time[busca], busca significa o indice do jogador na lista[time]. time[busca]["gols"] são os gols do jogador eslhido, pelo indice busca. Essa estrututa de repetição rodara o mesmo tanto de partidas q o jogador eslhido jogou, mostrando quantos gols ele fez em cada partida
            # i+1 indice da estruta serve para que possamos ver em qual partida o jogador fez tantos gols
            # g Quantidade de gols feitos naquela partida 
            print(f'   No jogo {i+1} fez {g} gols.')# Mosta o indice e a quantidade de gols feita na mesma 
            #OBs IMPORTANTE, Esse for roda apenas dentro (time[busca]["gols"]) q é igual a jogador['gols'] = partidas[:]
    print('-'*40)
print('<<VOLTE SEMPRE>>')#FIMMMMMMM









#Para que posso ser analisados os dados do código de maneira ampla
print('-='*30)
print(time)
print('-='*30)
print(jogador)
print('-='*30)
print(partidas)