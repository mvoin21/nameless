print('click enter to exit')
x = True
while x:
    x = input('Enter number: ')
    if x == '':
        print('"The end"')
        break
    elif int(x) == 0:
        print('0')
    elif int(x) % 2 == 0:
        print('1')
    elif int(x) % 2 != 0:
        print('-1')
    