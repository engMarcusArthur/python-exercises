larg = float(input('Digite a largura da parede (em metros): '))
alt = float(input('Digite a altura da parede (em metros): '))
area = larg * alt
print('A área da parede é {:.2f} m², sendo que, para pintá-la, será preciso {:.3f} l de tinta' .format(area, area / 2))
