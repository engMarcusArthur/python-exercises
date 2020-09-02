from random import shuffle
a1 = input('Digite o nome do primeiro aluno: ').capitalize()
a2 = input('Digite o nome do segundo aluno ').capitalize()
a3 = input('Digite o nome do terceiro aluno: ').capitalize()
a4 = input('Digite o nome do quarto aluno: ').capitalize()
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('''ORDEM DAS APRESENTAÇÕES
{}''' .format(alunos))
