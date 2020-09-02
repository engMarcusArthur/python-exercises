#analise de expressões matemáticas com parenteses
exp = input('Digite a expressão: ')
#pilha é uma lista de controle. caso no fim da execução do programa ela esteja vazia, a expressão será valida
pilha = list()

#nesse for, será analisado cada espaço da string exp
for simb in exp:
#se o espaço for igual ao (, ele será adicionado a lista pilha
    if simb == '(':
        pilha.append('(')
#senão, caso seja igual a ) e a pilha tiver algum espaço, a pilha terá um( removido, pois este terá encontrado um )
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
#senão, ao fim da pilha será adicionado )
        else:
            pilha.append(')')
            break
#verificação se a lista pilha está vazia - validando-a - ou com algum elemento - invalidando-a
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
