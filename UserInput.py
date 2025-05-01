# Input() = a function that prompts the user to enter data and returns it as a string. It is always a string, even if the user enters a number. You can use typecasting to convert it to the desired data type.
# I will show you how to use input() in Python as well as how to convert the input to the desired data type. There will be the first example and then we will explore how to use an f-string to format the output.

# Example 1: Using input() to get user input and typecasting it to an integer.
# In this example, we will ask the user to enter their name and birth year. We will then calculate their age based on the current year (2023) and print it out.
name = input('Enter your name: ')  # This will prompt the user to enter their name and wait for input.
print('Your name is ', name)

birth_year = int(input('Enter your birth year: '))  # This will prompt the user to enter their birth year and wait for input. 
age = 2023 - birth_year
print(age)

# Example 2: Using f-string to format the output.
# In this example, we will use an f-string to format the output and print the user's name and age in a single line.
name = input('Enter your name: ')  # This will prompt the user to enter their name and wait for input.
age =  int(input('Enter your age: '))

age = age + 1

print(f"Hello {name}!")  # This will print a greeting message using an f-string.
print("Have a great day!")
print(f"Your age is {age}.")  # This will print the user's age using an f-string.

# Exercise 1: Calculate the length and width of a rectangle
length = input("Enter the length: ")
width = input("Enter the width: ")
area = int(length) * int(width)
print(f" The area is: {area}cm^2")

# Exercise 2: Shopping cart program
item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like? "))
total = price * quantity
print(f"You have purchased {quantity} x {item}/s")
print(f"Your total is: ${total}")
