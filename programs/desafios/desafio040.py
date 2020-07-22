n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
    if m < 5:
        print('REPROVADO')
    elif m < 6.9:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')
else:
    print('Alguma das notas é inválida. Por favor, digite uma nota entre 0 e 10')
