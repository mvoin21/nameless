print('double click enter to exit')
a = True
while a:
    a = input('Enter first number: ')
    b = input('Entter second number: ')
    if a == '':
        print('"The end"')
        break
    elif int(a) > int(b):
        print('You should do like this: a <= b')
        continue
    elif int(a) <= int(b):
        c = [i for i in range(int(a), int(b)+1)]
        print(c)
