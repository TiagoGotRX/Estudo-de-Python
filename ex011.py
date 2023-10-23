larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
area=larg*alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}metros quadrados.'.format(larg, alt, area))
tinta= area/2
print('Para pintar essa parede, voce precisara de {}L de tinta.'.format(tinta))