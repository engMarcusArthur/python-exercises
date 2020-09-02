n = int(input('Digite um numero: '))
ni = n
cont = n - 1
while cont > 0:
    n = n * cont
    cont -= 1
print('{}! = {}' .format(ni, n))

for cont in range(cont, 0, -1):
    n = n * cont
print('{}! = {}' .format(ni, n))
