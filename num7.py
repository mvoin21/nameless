print('click enter to exit')
x = True
while x:
    x = input()
    if x == '':
        print('"The end"')
        break
    else:
        factorial = 1
        for i in range(1, int(x)+1):
            factorial *= i
        print(factorial)
