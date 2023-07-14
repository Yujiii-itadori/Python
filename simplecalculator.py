# simple calculator
x = int(input("Enter the first number: "))
y = input( "Enter an operator: ")
z = int(input("Enter the second number: "))

if y == '+':
    print(x + z)
elif  y == '-':
    print(x - z)
elif y == '/':
    print(x / z)
elif y == '%':
    print(x % z)
elif y == '**':
    print(x ** z)
else:
    print("Invalid operation")


