l1 = float(input('medida do lado A: '))
l2 = float(input('medida do lado B: '))
l3 = float(input('medida do lado C: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('Cada lado mede {:.1f}, formando, assim um triângulo equilátero' .format(l1, l2, l3))
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Lados de medidas {:.1f}, {:.1f} e {:.1f} formam um triângulo isósceles, onde pelo menos dois lados possuem o mesmo tamanho' .format(l1, l2, l3))
    else:
        print('Os lados medem {:.1f}, {:.1f} e {:.1f}, sendo que, como são diferentes, formam um triângulo escaleno' .format(l1, l2, l3))
else:
    print('{:.1f}, {:.1f} e {:.1f} não formam um triângulo' .format(l1, l2, l3))
