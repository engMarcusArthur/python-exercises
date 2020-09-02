num = list()
for cont in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {cont}: ')))
print(f'O maior valor digitado foi {max(num)} na(s) posição(ões) ', end='')
for i in range(0, len(num)):
    if num[i] == max(num):
        print(i, end=' ')
print(f'\nO menor valor digitado foi {min(num)} na(s) posição(ões) ', end='')
for j in range(0,len(num)):
    if num[j] == min(num):
        print(j, end=' ')
