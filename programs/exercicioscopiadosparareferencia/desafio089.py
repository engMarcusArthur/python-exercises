alunos = list()
while True:
    nome = input('Nome: ').strip().title()
    while True:
        while True:
            n1 = float(input('Nota 1: '))
            if n1 >= 0 and n1 <= 10:
                break
        while True:
            n2 = float(input('Nota 2: '))
            if n2 >= 0 and n2 <= 10:
                break
        med = (n1 + n2) / 2
        break
    alunos.append([nome, [n1, n2], med])
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp[0] == 'S' or resp[0] == 'N':
            break
    if resp[0] == 'N':
        print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":<5}')
        print('-' * 25)
        for i, v in enumerate(alunos):
            print(f'{i:<5}{v[0]:<10}{v[2]:<8}')
        print('-' * 25)
        while True:
            while True:
                resp = input('Deseja visualizar as notas de algum aluno? [S/N] ').strip().title()
                if resp[0] == 'S' or resp[0] == 'N':
                    break
            if resp[0] == 'S':
                cons = int(input('Digite o número do aluno: '))
                print(f'Notas do(a) {alunos[cons][0]}: {alunos[cons][1]}')
            else:
                break
        break
print('FIM')
