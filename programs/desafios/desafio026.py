frase = input('Digite uma frase: ').lower()
print('''A letra "a" aparece {} vezes, sendo que, pela primeira vez, na posição {}. A última aparição ocorre em {}''' .format(frase.count('a'), frase.find('a'), frase.rfind('a')))
