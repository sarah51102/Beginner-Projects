# These are the basic concepts of Python programming language. We will focus on arithmetic operations and data types.

print(3+2) # Addition, otuput: 5
print(3-2) # Subtraction, output: 1
print(3*2) # Multiplication, output: 6
print(3/2) # Division, output: 1.5
print(3**2) # Exponentiation, output: 9 (3^2)
print(3%2) # Modulus, output: 1 (remainder of 3 divided by 2)
print(3//2) # Floor Division, output: 1 (3 divided by 2, without the decimal part)
# This program demonstrates basic arithmetic operations in Python.


# Python can identify the type of data using type () function.
# The type of data is important in programming, as it determines what operations can be performed on the data.
# For example, you cannot add a string and an integer together, as they are different types of data.
# In Python, there are several built-in data types, including:

# 1. int: Integer, a whole number (e.g., 5, -3)
# 2. float: Floating-point number, a number with a decimal point (e.g., 3.14, -0.5) 
# 3. complex: Complex number, a number with a real and imaginary part (e.g., 2 + 3j)
# 4. str: String, a sequence of characters (e.g., "Hello, World!")
# 5. list: List, a collection of items (e.g., [1, 2, 3], ["apple", "banana"]) an ordered, changeable collection of items
#    - Lists can contain different data types, including other lists.
# 6. dict: Dictionary, a collection of key-value pairs (e.g., {"name": "Alice", "age": 25})
# 7. set: Set, a collection of unique items (e.g., {1, 2, 3}, {"apple", "banana"}) an unoredered, unindexed collection of unique items
#    - Sets are useful for removing duplicates from a list or for performing set operations like union and intersection.
# 8. tuple: Tuple, a collection of items that cannot be changed (e.g., (1, 2, 3), ("apple", "banana"))
# 9. bool: Boolean, a value that can be either True or False (e.g., True, False)

# Task 1: Basic Math Practice
# In this task, you will practice basic math operations in Python.
print("Practice Section")
result= 3 + 2
print(result) 
print(type(result)) 

result= 3-2
print(result)
print(type(result))

result= 5*2
print(result)
print(type(result))

result= 5/2
print(result)
print(type(result))

result= 5**2
print(result)
print(type(result))
# We are basically saying it is 5^2, which is 25.

result= 5%2
print(result)
print(type(result))
# We are basically saying it is 5 mod 2, which is 1. We are calculating the remainder when 5 is divided by 2, which is 1.

result= 5//2
print(result)
print(type(result))
# We are basically saying it is 5//2, which is 2. We are calculating the quotient when 5 is divided by 2, which is 2. (2 goes into 5 twice)
 

# Task 2: Identify the Data Type
# In this task, you will identify the data type of a given value.
# You can use the type() function to check the data type of a value.
print(type(25)) # int
print(type(3.14)) # float
print(type(2 + 3j)) # complex
print(type("Hello, World!")) # str
print(type([1, 2, 3])) # list
print(type({"name": "Alice", "age": 25})) # dict
print(type({1, 2, 3})) # set
print(type((1, 2, 3))) # tuple
print(type(True)) # bool
print(type(False)) # bool
