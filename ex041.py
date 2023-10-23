from datetime import date
idade = int(input('Digite em qual anos vc nasceu: '))
atual = date.today().year
clas =  atual - idade
if clas <= 9:
    print('O atleta tem {} e está na categoria MIRIN'.format(clas))
elif clas <= 14:
    print('O atleta tem {} e está na categoria INFANTIL'.format(clas))
elif clas <= 19:
    print('O atleta tem {} e está na categoria JUNIOR'.format(clas))
elif clas <= 25:
    print('O atleta tem {} e está na categoria SENIOR'.format(clas))
else:
    print('O atleta tem {} e está na categoria MASTER'.format(clas))