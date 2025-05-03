# Python Calculator

operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: ")) # Adding float() to convert string to float by typecstin them as floats.
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3)) # Round to 3 decimal places
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is an invalid operator")
