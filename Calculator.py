x=int(input('Please enter a number.'))

y=int(input('Please enter another number.'))

operation= input('Please enter the basic arithmetic operation: +,-,* or /:')

if operation == '+':
    print(x+y)
elif operation == '-':
    print(x-y)
elif operation == '*':
    print(x*y)
elif operation == '/':
    print(x/y)
else:
    print('Unrecognisable basic arithmetic operation')