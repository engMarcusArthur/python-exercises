from random import randint
n = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'''Os números sorteados foram: {n}
O maior número sorteado foi {max(n)} e o menor {min(n)}''')
