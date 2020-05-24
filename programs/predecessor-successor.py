#show the predecessor and successor of a number

while True:
    num = int(input('Type a number: '))
    #last and next exibition
    print(f'The predecessor of {num} is {num - 1} and the successor, {num + 1}')
    print('-' * 100)

    #continue or end
    while True:
        #strip to remove unwanted spaces; upper to uppercase
        ans = input('Do you wanted continue? [Y/N] ').strip().upper()
        #considering just the first character
        if ans[0] == 'Y' or ans[0] == 'N':
            print('-' * 100)
            break
    if ans[0] == 'N':
        break
print('END')
