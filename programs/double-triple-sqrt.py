def twice(x):
    """
        This function calculates the double, sending the result to the msg function
        x -> value entered by the user
        result -> the double of 'x'
    """
    result = x * 2
    msg('double', x, result)


def triple (x):
    """
        This function calculates the triple, sending the result to the msg function
        x -> value entered by the user
        result -> the triple of 'x'
    """
    result = x * 3
    msg('triple', x, result)


def squareRoot(x):
    """
        This function calculates the square root (sqrt), sending the result to the msg function
        x -> value entered by the user
        result -> the square root of 'x'
    """
    from math import sqrt
    result = f'{sqrt(x):.2f}'
    msg('square root', x, result)


def msg(action, x, result):
    """
        This function reports the result to the user
        action -> action taken to determine the result
        x -> value entered by the user
        result -> result of action on 'x'
    """
    print(f'The {action.title()} of {x} is: {result}')


def line():
    """This function show a line in the screen"""
    print('-' * 35)


#Main
n = int(input('Type a number: '))
line()
twice(n)
triple(n)
squareRoot(n)
line()
