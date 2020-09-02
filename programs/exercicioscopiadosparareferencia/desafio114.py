import urllib
import urllib.request

cores = {'vermelho': '\033[1;31m', 'azul': '\033[1;34m'}
site = 'http://www.pudim.com.br'
test = urllib.request.urlopen(site)
'''
try:
    test = urllib.request.urlopen(site)

except urllib.error.URLError:
    print(f'{cores["vermelho"]}{site} está off-line')
else:
    print(f'{cores["azul"]}{site} está on-line')
    print(test.read())
'''