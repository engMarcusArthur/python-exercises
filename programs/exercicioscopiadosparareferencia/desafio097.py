def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva(
    input('Digite uma mensagem: ').strip().title()
)
