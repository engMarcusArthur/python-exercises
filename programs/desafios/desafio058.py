from random import randint
npc = randint(1, 10)
nuser = 11
tent = 0
while nuser != npc:
    nuser = int(input('Adivinhe o número que estou pensando: '))
    if nuser >= 0 and nuser <= 10:
        if nuser != npc:
            print('Não estou pensando em {}... tente novamente!\n' .format(nuser))
            tent += 1
        else:
            print('Você acertou! Foram necessárias {} tentativas para acertar o número {}\n' .format(tent, nuser))
    else:
        print('Por favor, digite somente números entre 0 e 10\n')
        tent += 1
