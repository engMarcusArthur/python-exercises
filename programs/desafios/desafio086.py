matriz = [[], [], []]
sp = s3 = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print(f"{'Matriz': ^20}", end='')
for i in range(0, len(matriz)):
    print('\n|', end='')
    for j in range(0, len(matriz[i])):
        print(f'{matriz[i][j]: ^5}', end='|')
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            sp += matriz[i][j]
for l in range(0, 3):
    s3 += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        m = matriz[1][c]
    elif m < matriz[1][c]:
        m = matriz[1][c]
print(f'\nA soma dos valores pares é {sp}, e, da terceira coluna, {s3}. O maior numero da segunda linha é {m}')
