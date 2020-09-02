from random import randint

npc = randint(0, 5)
nu = int(input('Adivinhe o número que estou pensando: '))

if nu == npc:
    print('Você venceu! Eu estava pensando em {}' .format(npc))
else:
    print('Você perdeu! Eu estava pensando em {}' .format(npc))
