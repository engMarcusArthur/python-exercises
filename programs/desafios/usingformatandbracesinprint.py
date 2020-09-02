n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
print('The sum between {} and {} is {}.' .format(n1, n2, n1 + n2))
#You can chance the printing values order just informing the position between the braces, like this:
print('{2} minus {0} is equal to {1}.' .format(n1, n2, n1 + n2))
input()