from datetime import date

s = 0
m = 0
for i in range(0, 6):
    ano = int(input('Digite o ano de nascimento: '))
    if date.today().year - ano >= 21:
        s = s + 1
    else:
        m = m + 1
print('{} pessoas são maiores de idade e {} ainda são menores' .format(s, m))

