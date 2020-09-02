#control variables
adult = man = woman20 = 0

while True:
    #user data
    gender = comand = ''
    line = '=' * 30
    print(line)
    age = int(input('Your age: '))
    while gender != 'M' and gender != 'F':
        gender = input('Your gender (M/F): ').strip().upper()
        gender = gender[0]
    #conditionais for control variables addictions
    #age control
    if age > 18:
        adult += 1
    #man control
    if gender == 'M':
        man += 1
    #woman20 control
    elif gender != 'M' and age < 20:
        woman20 += 1
    #control of restart or ended
    while comand != 'Y' and comand != 'N':
        comand = input('Do you want continue? [y/n] ').strip().upper()
        comand = comand[0]
    if comand != 'Y':
        print(line)
        print(f'{adult} people has most 18 years and {man} users was men. Between women, {woman20} say(id) has less 20 years old')
        break

print('END')
