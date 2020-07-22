n = int(input('Digite um valor: ')), int(input('Digite um valor: ')), \
    int(input('Digite um valor: ')), int(input('Digite um valor: '))
print(f'O valor 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Valor(es) par(es): ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')
