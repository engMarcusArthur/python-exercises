def leiaDinheiro(msg):
    from time import sleep
    cores = {'normal':'\033[0;0m', 'vermelho':'\033[1;31m','verde':'\033[0;32m'}
    
    while True:
        v = input(f'{msg}').strip().replace(',', '.')
        sleep(1)
        if v.isalpha():
            print(f'{cores["vermelho"]}"{v}" é um preço inválido. Tente novamente!{cores["normal"]}')
        elif v == '':
            print(f'{cores["vermelho"]}Campo "VALOR MONETÁRIO" é obrigatório. Tente novamente!{cores["normal"]}')
        else:
            print(f'{cores["verde"]}{v} é válido! Analisando dados...{cores["normal"]}')
            break
        sleep(1)
    return float(v)

