#Program that reads a user's input and presents some characteristics of that string

while True:
    #this variable is called key because abbreviates "keyboard"
    key = input('Type something: ')

    print('-' * 100)
    # verification to number or/and word
    if True == key.isalnum() or True == key.strip().isalnum():
        #key.strip() to remove unwanted spaces
        key = key.strip()
        print(f'"{key}" is alphanumeric,', end='')
        if key.isnumeric() == True:
            print(' and is a number')
        else:
            print(' and is a word')

        #word lower or uppercase
            if True == key.islower():
                print(f'"{key}" is lowercase')
            else:
                print(f'"{key}" is uppercase')

    # 'key' has only spaces:
    elif True == key.isspace():
        print(f'The input contains only spaces')

    #'key' isn't a number or word or spaces
    else:
        print(f"'{key}' isn't a number/word, nor does it have spaces only", end='')
        #verification to sentence
        for i in key.strip():
            if True == i.isalnum():
                print(", but it's a sentence")
                break
            elif i == key[-1] and False == i.isalnum():
                print(', nor is it a sentence')
    print('-' * 100)

    #to continues typing or to end
    while True:
        #.strip() to remove unwanted spaces, and .upper() to uppercase
        answer = input('Do you want continue? [Y/N] ').strip().upper()
        #[0] to read only the first letter, if the user has typed the entire word
        if answer[0] == 'Y' or answer[0] == 'N':
            break
    print('-' * 100)
    if answer[0] == 'N':
        break
print('END')