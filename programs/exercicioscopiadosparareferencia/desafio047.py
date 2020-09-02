print('Mostrando números pares entre 1 e 50')
for i in range(1, 50 + 1):
    if i % 2 == 0:
        print('{} - ' .format(i), end = '')
        i = i + 2
    else:
        i = i + 1
print('\nFIM')
