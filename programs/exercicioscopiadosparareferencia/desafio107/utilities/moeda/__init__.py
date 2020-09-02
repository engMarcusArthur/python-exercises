def metade(v, form = True):
    result = v / 2
    if form:
        return moeda(result)
    else:
        return result


def dobro(v, form=True):
    result = v * 2
    if form:
        return moeda(result)
    else:
        return result


def aumentar(v, percent, form=True):
    result = v * (1 + (percent / 100))
    if form:
        return moeda(result)
    else:
        return result


def diminuir(v, percent, form=True):
    result = v * (1 - (percent / 100))
    if form:
        return moeda(result)
    else:
        return  result


def moeda(v):
    return f'R$ {v:.2f}'


def linha():
    print('-' * 30)


def resumo(v, aum, dim):
    linha()
    print(f'{"RESUMO DO VALOR": ^30}')
    linha()
    print(f"{'Preço Analisado:': <20}{moeda(v): <10}")
    print(f"{'Dobro do Preço:': <20}{dobro(v): <10}")
    print(f"{'80% do Aumento:': <20}{aumentar(v, aum): <10}")
    print(f"{'35% de Redução:': <20}{diminuir(v, dim): <10}")
    linha()
    