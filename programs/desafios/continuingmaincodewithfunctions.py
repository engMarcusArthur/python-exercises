# A function continuing() enchained with a function main() to reiterate the code until type N and Enter

# Definying the function of continuity
def continuing():
    answer = input('To exit type N and press Enter: ').strip().upper()
    answer+='anything'
    if answer[0] != 'N':
        print('-' * 100, 'CONTINUING:','-' * 100,'\n')
        main()
        return
    input("OK, press Enter again, please.")
    return

# Using the function above and putting your main code inside a function main() and calling the function above on the ending of the main you can create a reiteration of your testing codes.

def main(): # Definying the function with the main code
    key = input('Type something: ')
    print('-' * 100)
    if True == key.isalnum() or True == key.strip().isalnum():
        key = key.strip()
        print(f'"{key}" is alphanumeric,', end='')
        if key.isnumeric() == True:
            print(' and is a number')
        else:
            print(' and is a word')
            if True == key.islower():
                print(f'"{key}" is lowercase')
            else:
                print(f'"{key}" is uppercase')
    elif True == key.isspace():
        print(f'The input contains only spaces')
    else:
        print(f"'{key}' isn't a number/word, nor does it have spaces only", end='')
        for i in key.strip():
            if True == i.isalnum():
                print(", but it seems to be a sentence.")
                break
            elif i == key[-1] and False == i.isalnum():
                print(', nor is it a sentence.')
    print('-' * 100)
    continuing() # Call function continuing() and verify if the user wants to continue

main()

print('END')
