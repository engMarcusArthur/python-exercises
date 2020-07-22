from random import randint
print('''\033[7mJOKENPÔ\033[m
Como escolher a posição?
Bastará digitar:
1. Pedra
2. Papel
3. Tesoura
Eu escolherei o meu no mesmo instante. Vamos jogar?''')

pc = randint(1, 3)
user = int(input('Digite 1 para pedra, 2 para papel ou 3 para tesoura: '))

print('JO KEN PÔ!\n')
if user == pc:
    print('EMPATE! Ambos selecionaram {}' .format(user))
elif user == 1:
    if pc == 2:
        print('PERDEDOR!\nEu escolhi papel, e papel embrulha a pedra')
    else:
        print('ME VENCEU DESSA VEZ!\nEu escolhi tesoura, e a sua pedra me quebrou')
elif user == 2:
    if pc == 1:
        print('ME VENCEU DESSA VEZ!\nEu escolhi pedra, e o seu papel me embrulhou')
    else:
        print('PERDEDOR!\nEu escolhi tesoura, e te cortei')
elif user == 3:
    if pc == 1:
        print('PERDEDOR!\nMinha pedra quebrou a sua tesoura')
    else:
        print('ME VENCEU DESSA VEZ!\nVocê acabou me cortando')
else:
    print('Você escolheu um valor inválido. Por favor, reinicie o jogo')
