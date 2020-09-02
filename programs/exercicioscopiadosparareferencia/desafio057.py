gender = ''
i = 0
while gender != 'M' or gender != 'F' and i == 0:
    gender = input('Digite o seu genero (M/F): ').upper()
    gender = gender[0]
    if gender != 'M' and gender != 'F':
        print('Valor inválido\n')
    else:
        i = 1
print('Fim')
