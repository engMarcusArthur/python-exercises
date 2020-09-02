fraseo = input('Escreva uma frase (sem acento e pontuação): ')
frase = fraseo.lower().split()
words = len(frase)
nospace = frase[0]

for i in range(1, words):
    nospace = nospace + frase[i]

if nospace == nospace[::-1]:
    print('A frase "{}" é um políndromo' .format(fraseo))
else:
    print('A frase "{}" não é um políndromo' .format(fraseo))
