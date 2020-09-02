l1 = float(input('medida do lado A: '))
l2 = float(input('medida do lado B: '))
l3 = float(input('medida do lado C: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('{:.1f}, {:.1f} e {:.1f} formam um triângulo' .format(l1, l2, l3))
else:
    print('{:.1f}, {:.1f} e {:.1f} não formam um triângulo' .format(l1, l2, l3))
