def linha():
    '''
    -> essa função adiciona uma linha
    '''
    print('~~' * 15)


def validacao(nasc):
    '''
    -> essa função verifica se o ano digitado pelo usuário é válido, lendo fazendo comparações com o ano atual e com o ano 1890, verificando se faz sentido
    :param nasc: ano digitado pelo usuário
    :return: caso os dados estejam coerentes, retornará o bool False para poder sair do looping em uma verificação externa
    '''
    from datetime import date
    if nasc < 1890 or nasc > date.today().year:
        print('Ano de Nascimento inválido. Tente Novamente')
        return True
    else:
        print('Ano válido. Analisando...')
        return False


def voto(age):
    '''
    -> Função que retorna, baseado na idade do usuário, a situação eleitoral do mesmo
    :param age: variavel global ano(informada pelo usuário) - ano atual
    :return: valor literal informando a situação literal baseada no valor da variável age
    '''
    from datetime import date
    age = date.today().year - age
    if age < 16:
        return f'NÃO VOTA com {age} anos.'
    elif 18 <= age <= 65:
        return f'VOTO OBRIGATÓRIO com {age} anos.'
    else:
        return f'VOTO OPCIONAL com {age} anos.'


# Programa Principal
linha()
while True:
    ano = int(input('Ano de Nascimento: '))
    if validacao(ano) is False:
        break
print(voto(ano))

