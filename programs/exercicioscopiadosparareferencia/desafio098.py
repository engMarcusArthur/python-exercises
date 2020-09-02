#para dar a sensação de realmente ser um contador
from time import sleep


# para adicionar a linha divisoria sem varios prints
def linha():
    print('=-' * 20)
    sleep(0.25)


# irá exibir varias contagens
def contador(inicio, fim, passo):
    sleep(0.25)
    print(f'Contagem de {inicio} à {fim}, de {passo} em {passo}:')
    sleep(1.5)
    # ANALISE DOS DADOS DE ENTRADA
    # passo = 0 será considerado = 1
    if passo == 0:
        passo = 1
    if inicio > fim:
        # correção de um possivel erro para contagem decrescente
        if passo > 0:
            passo *= -1
        # em caso de contagem decrescente, o programa seguirá esse bloco
        while inicio >= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += passo
            sleep(0.5)
    # contagem crescente será o bloco seguinte
    else:
        if passo < 0:
            passo *= -1
        while inicio <= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += passo
            sleep(0.5)
    print()


#Programa principal
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('AGORA É A SUA VEZ!')
sleep(1)
contador(
    int(input('Inicio: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)
linha()