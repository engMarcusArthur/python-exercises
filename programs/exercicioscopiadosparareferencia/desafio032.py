year = int(input('Digite o ano: '))

if year > 1582 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} é bissexto' .format(year))
else:
    print('{} não é bissexto' . format(year))
