from random import randint
s = 0
print('Par ou ímpar')
while True:
    pc = randint(0, 5)
    rest = 2
    while rest != 0 and rest != 1:
        rest = int(input('Par (0) ou ímpar (1)? '))
    player = int(input('Jogue de 0 à 5, como se fosse a sua mão: '))
    if player < 0 or player > 5:
        print('Valor inválido. Você perdeu')
        if s > 0:
            print(f'Você venceu {s} rodadas')
        break
    elif (pc + player) % 2 == rest:
        print('Você ganhou')
        s += 1
    else:
        print('Você perdeu')
        break
if s > 0:
    print(f'Você venceu {s} rodadas')
