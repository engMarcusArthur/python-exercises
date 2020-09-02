lista = [[], []]
for i in range(1, 8):
    v = int(input(f'Digite o {i}º valor: '))
    if v % 2 == 0:
        lista[0].append(v)
        lista[0] = sorted(lista[0])
    else:
        lista[1].append(v)
        lista[1] = sorted(lista[1])
print(f'Os números pares digitados foram {lista[0]}, e, os ímpares, {lista[1]}')
