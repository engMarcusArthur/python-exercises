from lib.interface import *
from time import sleep

while True:
    resp = menu(['Visualizar Cadastrados', 'Novo Cadastro', 'Encerrar'])
    if resp == 1 or resp == 2:
        cabecalho('Sucesso')
    elif resp == 3:
        cabecalho('Encerrando o sistema... Volte sempre')
        break
    else:
        print('\033[31mERRO! Por favor, digite uma opção válida\033[m')
    sleep(2)
