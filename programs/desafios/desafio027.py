nome = input('Digite o seu nome completo: ').strip().title()
nome = nome.split()
print('{} {}' .format(nome[0], nome[len(nome) - 1]))
