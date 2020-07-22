def proximo():
    '''
    -> função que indica se a inserção continuará ou não
    :return: resp, s para continuar e n para parar
    '''
    while True:
        resp = input('Deseja continuar? [S/N] ').strip()[0]
        if resp in 'SsNn':
            break
        print('Por favor, responda com "sim" ou "não"')
    return resp


def verificacaoNota(nota):
    '''
    -> função que verifica se a nota está dentro dos padrões, ou seja, ]0, 10[, sendo que, caso esteja, a nota será adicionada a uma lista
    :param nota: input com a nota inserida
    :return: booleano indicando True caso a operação tenha falhado e False caso o looping externo não precise repetir
    '''
    if nota >= 0 and nota <= 10:
        lista.append(nota)
        sit = False
    else:
        print('Digite uma nota entre 0 e 10')
        sit = True
    return sit


def notas(n):
    '''
    -> função que retorna as informações sobre as notas de alunos em forma de dicionário
    :param n: notas inseridas
    :return: dicionário com a quantidade de notas, maior nota, menor nota e média, além da situação, caso deseje-se vizualizá-la
    '''
    retorno = dict()
    retorno['Quantidade de Notas'] = len(n)
    retorno['Maior Nota'] = max(n)
    retorno['Menor Nota'] = min(n)
    retorno['Média'] = sum(n) / retorno['Quantidade de Notas']
    while True:
        sit = input('Deseja exibir a situação? [S/N] ').strip()[0]
        if sit in 'SsNn':
            break
        print('Por favor, responda com "sim" ou "não"')
    if sit in 'Ss':
        if retorno['Média'] >= 7:
            retorno['Situação'] = 'Boa'
        elif retorno['Média'] >= 5:
            retorno['Situação'] = 'Razoável'
        else:
            retorno['Situação'] = 'Ruim'
    retorno['Média'] = float(f"{retorno['Média']:.2f}")
    return retorno


lista = list()
while True:
    while True:
        if verificacaoNota(float(input('Digite uma nota: '))) is False:
            break
    if proximo() in 'Nn':
        break
print(notas(lista))
help(notas)