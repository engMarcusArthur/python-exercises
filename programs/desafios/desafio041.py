from datetime import date

birth = int(input('Ano de nascimento do atleta: '))
yo = date.today().year - birth

if yo <= 9:
    print('MIRIM')
elif yo <= 14:
    print('INFANTIL')
elif yo <= 19:
    print('JUNIOR')
elif yo <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
