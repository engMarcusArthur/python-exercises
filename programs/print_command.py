#A section with examples of command print sintaxis

a=1
b="'word'"
c=1.34
ite=0
print("<1>%d is an integer while %s is a string."%(a,b))
print("<2>%s is a string and %s too."%(a,b)) #'a' is converted to string
print("<3>{} is an integer while {} is a string.".format(a,b))
print("<4>{1} is a string while {0} is an integer and {2} is a float.".format(a,b,c))
print(f'<5>{b} is a string while {a} is an integer and {c} is a float.')
print('<6>We can cite one element more than once: {1} and {1}'.format(a,b,c))
print("<7>",a,"is an integer",b,"is a string and",c,'is a float')
sometyped = input("Type something -->")
print("<8>You have just typed: ", end='')
print(sometyped)
print("<9>You have just typed: ")
print(sometyped)
print("<10>You have just typed: ", sometyped)
try:
    n1 = float(input('Digite o valor em metros: '))
    print('<11>{:.2f} m is the same as {:.0f} cm and {:.0f} mm' .format(n1, n1 * 100, n1 * 1000))
except:
    print('Something went wrong.')
    print('You must to type a float number and ', end='')
    print('to use point to separate the decimal part of the number (not comma).')
    
input()