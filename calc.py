# Python calculator

operator = input('Choose an operator (+ - * /): ')
num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(round(result, 4))
else:
    print('Enter correct operator!' )