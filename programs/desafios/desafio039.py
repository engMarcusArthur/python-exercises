from datetime import date

birth = int(input('Informe o ano do seu nascimento: '))
yo = date.today().year - birth

print('Você completará {} anos em {}' .format(yo, date.today().year))

if yo == 18:
    print('Você deve alistar-se esse ano!')
elif yo < 18:
    print('Você deverá se alistar daqui {} anos' .format(18 - yo))
else:
    print('Você deveria ter se alistado há {} anos' .format(yo - 18))
