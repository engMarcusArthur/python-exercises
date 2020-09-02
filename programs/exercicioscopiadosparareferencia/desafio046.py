from time import sleep
from emoji import emojize

print('CONTAGEM REGRESSIVA')
sleep(1)

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emojize(':fireworks: ' * 50))
