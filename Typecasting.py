# Typecasting = the process of converting one data type into another and is especially useful when you are working with user input, as it is always a string.
# str(), int(), float(), bool() are the most common typecasting functions

name = "Ellis"
age = "28"
gpa = 1.75
is_student = True

print(type(name)) # <class 'str'>


# Convert age to an integer
gpa = int(gpa)
print(gpa) # <class 'int'>

# Convert age to a float
age = float(age)
print(age) # <class 'float'>

# Conevert age to a string
age = str(age)
print(type(age)) # <class 'str'>
# To prove that it is a string, you will type it like so: print(float(age)) 

# Convert age to a boolean
# This will convert any non-empty string to True and an empty string to False
name = bool(name)
print(name) # <class 'bool'>
