h = float(input('Altura (m): '))
p = float(input('Peso (Kg): '))
imc = p / h ** 2

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está em seu peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')

