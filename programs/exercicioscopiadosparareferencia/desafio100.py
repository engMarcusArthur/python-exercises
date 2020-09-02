from random import randint


def sorteia(num):
    for i in range(0, 5):
        while True:
            v = randint(1, 10)
            if v not in num:
                num.append(v)
                break
    print(f'Os números sorteados foram {sorted(num)}')


def somaPar(num):
    s = 0
    for j in num:
        if j % 2 == 0:
            s += j
    print(f'A soma dos valores pares sorteados é {s}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
