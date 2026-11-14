a = int(input('первое число '))
b = int(input("второе число "))
c = input('операция ')
if c == '+':
    print('Результат ' + str(a+b))
elif c == '-':
    print('Результат ' + str(a-b))
elif c == '*':
    print('Результат ' + str(a*b))
elif c =='/':
        if b == 0 :
             print("деление на ноль")
        print('Результат ' + str(a/b))

