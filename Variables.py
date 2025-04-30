# Python Variables
# Variables are used to store data values. In Python, variables do not need to be declared with a specific type, as Python is dynamically typed.
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
