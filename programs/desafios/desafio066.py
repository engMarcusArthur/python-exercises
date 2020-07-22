s = qtd = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        print(f'Foram digitados {qtd} números, sendo a soma entre eles {s}')
        break
    qtd += 1
    s += n
