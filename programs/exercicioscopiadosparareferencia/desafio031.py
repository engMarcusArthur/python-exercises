dist = float(input('Distância (em Km) ao destino: '))

if dist <= 200:
    print('Valor da passagem: R$ {:.2f}' .format(dist/2))
else:
    print('Valor da passagem: R$ {:.2f}' .format(dist * 0.45))
