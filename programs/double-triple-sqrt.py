#print the double, triple and square root of a number typed by the user

#interesting to import 'sqrt' for square root resolution
from math import sqrt
# sqrt(x) returns the square root of 'x'

while True:
    num = int(input('Type a number: '))
    #here, the results will are printeds
    print(f'The double of {num} is {num * 2}; triple, {num * 3}; and the square root is {sqrt(num):.1f}\n')

    #continue or end
    while True:
        #strip to remove unwanted spaces; upper to uppercase
        ans = input('Do you wanted continue? [Y/N]').strip().upper()
        #considering just the first letter
        if ans[0] == 'Y' or ans[0] == 'N':
            break
    print('-' * 100)
    if ans[0] == 'N':
        break
print('END')
