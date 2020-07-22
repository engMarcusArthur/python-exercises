from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
ang = radians(ang)
print("""Para o angulo de {:.2f} rad, temos:
Seno = {:.2f} rad
Cosseno = {:.2f} rad
Tangente = {:.2f} rad""" .format(ang, sin(ang), cos(ang), tan(ang)))
