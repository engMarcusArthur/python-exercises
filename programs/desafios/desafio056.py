agegp = 0
maisvelho = 0
mulheres = 0
homem = ''
for i in range(0, 4):
    print('{}ª PESSOA' .format(i + 1))
    nome = input('Digite o seu nome: ').strip()
    idade = int(input('Digite a sua idade: '))
    sexo = int(input('Digite 1 para masculino e 2 para feminino: '))
    agegp += idade
    if idade > maisvelho and sexo == 1:
        maisvelho = idade
        homem = nome.title()
    elif idade < 20 and sexo == 2:
        mulheres += 1
print('''A média de idade do grupo é {}
O homem mais velho é {}
{} mulher(es) tem menos de 20 anos''' .format(agegp / 4, homem, mulheres))
