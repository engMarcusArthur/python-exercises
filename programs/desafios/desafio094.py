dados = dict()
lista = list()
s = 0
while True:
    dados['nome'] = input('Nome: ').strip().title()
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').strip()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('Genero invalido. Tente novamente')
    while True:
        dados['idade'] = int(input('Idade: '))
        if dados['idade'] > 0:
            s += dados['idade']
            break
        print(f"A idade {dados['idade']} é inválida, pois é negativa. Tente novamente")
    lista.append(dados.copy())
    dados.clear()
    while True:
        resp = input('Deseja continuar? [S/N] ').strip()
        if resp[0] in 'SsNn':
            break
        print('Resposta inválida. Tente novamente')
    if resp in 'Nn':
        break
print('-' * 30)
print(f'Ao todo, temos {len(lista)} pessoas cadastradas')
med = s / len(lista)
print(f'A idade média é {med:.2f}')
print(f'Lista de mulheres cadastradas:')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f" - {p['nome']}")
print('Lista de pessoas com idade superior à média:')
for p in lista:
    if p['idade'] >= med:
        print(f" - {p['nome']}: {p['idade']} anos")
print('=' * 30)
