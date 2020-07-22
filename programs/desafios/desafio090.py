dataluno = dict()
dataluno['nome'] = input('Nome: ').strip().title()
while True:
    dataluno['media'] = float(input(f"Média de {dataluno['nome'].upper()}: "))
    if dataluno['media'] < 0 or dataluno['media'] > 10:
        print(f"Desculpe, mas há algo errado... é impossível obter a média {dataluno['media']:.2f}. Tente novamente")
    else:
        if dataluno['media'] >= 7:
            dataluno['sit'] = 'aprovado(a)'
        elif dataluno['media'] >= 5:
            dataluno['sit'] = 'de recuperação'
        else:
            dataluno['sit'] = 'reprovado(a)'
        break
print(f"O(a) aluno(a) {dataluno['nome']} tem a média igual a {dataluno['media']:.2f}. Portanto, está {dataluno['sit'].upper()}")
