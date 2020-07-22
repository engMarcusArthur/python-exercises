from datetime import date
citizen = dict()
citizen['nome'] = input('Nome: ').strip().title()
while True:
    citizen['idade'] = date.today().year - int(input('Ano de Nascimento: '))
    if citizen['idade'] > date.today().year or citizen['idade'] <= 0:
        print('Ano de nascimento inválido. Tente novamente')
    else:
        break
while True:
    citizen['ctps'] = int(input('ctps: '))
    if citizen['ctps'] < 0:
        print('CTPS inválida. Tente novamente')
    elif citizen['ctps'] == 0:
        break
    else:
        while True:
            citizen['contratacao'] = int(input('Digite o ano de contração: '))
            if citizen['contratacao'] < date.today().year - citizen['idade'] or citizen['contratacao'] > date.today().year:
                print('Ano de contratação impossível de acordo com o ano corrente ou sua idade. Tente novamente')
            else:
                break
        while True:
            citizen['salario'] = float(input('Digite o salario: R$ '))
            if citizen['salario'] < 0:
                print('Valor de salário inválido. Tente novamente')
            else:
                break
        citizen['aposentadoria'] = citizen['contratacao'] - (date.today().year - citizen['idade']) + 35
        break
    print('Valores preenchidos com sucesso')
for k, v in citizen.items():
    print(f"{k.title()}: {v}")
