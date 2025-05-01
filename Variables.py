# Python Variables
# Variables are used to store data values (string, integer, float,boolean). In Python, variables do not need to be declared with a specific type, as Python is dynamically typed.
# This means that the type of a variable is determined at runtime based on the value assigned to it.

# Practice Task 1: Create Your Own Profile 
first_name = 'Ellis'
last_name = 'Romano'
country = 'Monaco'
city = 'Saint-Roman'
age = 238
is_married = True
# These are simple variables holding string, integer, and boolean values.

# Practice Task 2: Create Dictionary
# A dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value.
person_info = {
	'first_name': 'Ellis',
	'last_name': 'Romano',
	'country': 'Monaco',
	'city': 'Saint-Roman',
	'age': 238,
    'is_married': True,
}

# Practice Task 3: Print Information
# Print the values of the variables and dictionary keys
print('---My Profile---')
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is_Married:', is_married)
print('---My Profile from Dictionary---')


# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Ellis', 'Romano', 'Monaco', 238, True
    #Here, we are declaring multiple variables in one line and assigning values to them.
print(first_name, last_name, country, age, is_married)
print('---My Profile from Dictionary---')

# Extra Notes
# Another way to assign variables to the same line could look like this: x, y, z, = 1, 2, 3 (this is referred to as multiple assignment and do not forget that if you want it to print, put print(x) and then the rest on lines below)
# If you want to set variables to the same value, you can do it like this: x = y = z = 1 (this is referred to as chained assignment and do not forget that if you want it to print, put print(x) and then the rest on lines below)

# Strings- a series of texts with double or single quotes
first_name = 'Ellis'
print(first_name)
# OR use an f-string (the f means format) ex: print(f'Hello {first_name}') it is becoming more popular in coding, so I will use that for the other examples
email = 'ellisr123@fake.com'
print(f"Your email is {email}")

# Intergers- whole numbers (positive or negative) without decimals, of unlimited length without quotes because then it would become a string
age = 28
print("f'Your age is {age}')")
quantity = 1000
print(f'Your quantity is {quantity}')

# Floats- means floating point numbers, or decimal numbers 
price = 19.99
print(f'Your price is {price}')
gpa = 3.75
print(f'Your GPA is {gpa}')

# Booleans- a data type that can only be True or False, 1 or 0, yes or no, on or off, etc.
is_student = True
for_sale = False
print(f'Is the item for sale? {for_sale}')
print(f'Are you a student? {is_student}')

# You are more likely to see them used in if-else statements such as this:
if is_student:
    print('You are a student')
else:
    print('You are not a student')

if for_sale:
	print('The item is for sale')
else:
	print('The item is not for sale')	
