n = 0
while True:
    print('~'*45)
    n = int(input('Quer ver a tabuada de qual numero? '))
    print('~'*45)
    if n <= -0:
        print('Program encerrado')
        break
    for c in range(0, 10+1):
        print(f'{n} x {c} = {n*c}')
