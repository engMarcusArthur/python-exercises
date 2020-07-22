nome = input('Digite o seu nome: ')
separado = nome.split()
print('''{}
{}
O nome completo possui {} letras, sendo que o primeiro tem {} caracteres''' .format(nome.upper(), nome.lower(), len(''.join(separado)), len(separado[0])))
