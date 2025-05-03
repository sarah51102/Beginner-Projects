# if = do some code if condition is True
# else = do something else

age = int(input("Enter your age: "))
if age == 18:
    print("You are eligible for consideration.")
elif age < 0:
    print("Invalid age entered.")
elif age >= 35:
    print("You are eligible for a senior position.")
else:
    print("You must be 18+ to apply.")

# Notes
# 1. We can check more than one condition before reaching the else statement.
# 2. Elif means else if, and it is used to check multiple conditions.
# 3. ALWAYS pay attention to the order of the conditions.
# 4. With if statements, you can either use a condition or a boolean.

# Practice Section
response = input("Do you want to continue? (yes/no): ")
if response == "yes":
    print("Continuing...")
elif response == "no":
    print("Exiting...")
else:
    print("Invalid response. Please enter 'yes' or 'no'.")


name = input("Enter your name: ")
if name == "":
    print("You did not enter a name.")
else:
    print(f"Hello, {name}!")

# Example of a Boolean Variable
# Boolean variables can be used in place of a condition because a condition would evaluate to True or False.

# Define the for_sale variable
available_for_rent = True  # or False, depending on the desired initial value

if available_for_rent:
    print("This property is for sale.")
else:
    print("The property is not for sale.")
