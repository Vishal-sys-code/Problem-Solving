print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f


a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
celcius = int(input("Enter the Celcius: "))
operator = input('Enter the Operator: ')
if operator == '+':
    print('You have chosen addition')
    print(f'The answer is {a + b}')
elif operator == '-':
    print('You have chosen subtraction')
    print(f'The answer is {a - b}')
elif operator == '*':
    print('You have chosen multiplication')
    print(f'The answer is {a * b}')
elif operator == '/':
    print('You have chosen division')
    if b != 0:
        print(f'The answer is {a / b}')
    else:
        print('Error! Division by zero is not allowed')
else:
    print('Invalid operator.')
    print(f'The answer is {celcius * 9 / 5 + 32}')


# Approach 2
mode = input('Enter the math operation or f for Celcius to Fahrenheit Conversion: ')
num1 = float(input("Enter the First Number: "))
if mode.lower() == 'f':
    print(f'{num1} Celcius is equivalent to the {num1*9/5 + 32} fahrenheit')
else:
    num2 = int(input("Enter the Second Number: "))
    if mode == '+':
        print("f {Answer is: {num1 + num2}}")
    elif mode == '-':
        print(f"Answer is: {num1 - num2}")
    elif mode == '*':
        print(f"Answer is: {num1 * num2}")
    elif mode == '/':
        if num2 != 0:
            print(f"Answer is: {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed")
    else:
        print("Invalid operator.")