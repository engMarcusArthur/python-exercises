def linha():
    print('-' * 50)


def area(comp, larg):
    metroq = comp * larg
    print(f'A área do terreno de {larg:.2f}m x {comp:.2f}m é {metroq:.2f}m²')


print(f'{"CONTROLE DE TERRENOS": ^50}')
linha()
area(
    float(input('COMPRIMENTO(m): ')),
    float(input('LARGURA(m): '))
)
