maior = 0
menor = 0
for i in range(0, 5):
    p = float(input('Digite o seu peso: '))
    if i == 0:
        maior = p
        menor = p
    elif i > 0:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print('O maior peso foi {:.3f} Kg e o menor foi {:.3f} Kg' .format(maior, menor))
