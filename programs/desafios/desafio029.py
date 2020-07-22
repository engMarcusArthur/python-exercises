vel = int(input('Velocidade do carro (em Km/h): '))

if vel > 80:
    print('VOCÊ ESTÁ {} Km/h ACIMA DO LIMITE DE 80 Km/h! A multa será de RS {},00' .format(vel - 80, (vel - 80) * 7))
else:
    print('Você está dentro do limite de 80 Km/h')
