# Define variables of various data types and print them to observe how they are represented in Python.
our_integer = 10
our_float = 20.5
our_string = "Hello, Python!"
our_bool = True
print(our_integer, our_float, our_string, our_bool)

# Use type() to determine the data type of each variable. 
print(type(our_integer), type(our_float), type(our_string), type(our_bool))

# Modify the values of the variables to see how Python handles changes in type dynamically. Change integer to a string, float to boolean, etc.
new_integer = "Now I'm a string."
new_float = False
new_string = 42
new_bool = 3.14
print(new_integer, type(new_integer))
print(new_float, type(new_float))
print(new_string, type(new_string))
print(new_bool, type(new_bool))

# Practice 1: Create variables of different data types and display them.
my_integer = 100
my_float = 25.5
my_string = "Learn Python!"
my_boolean = True
my_list = [5, 10, 15]

# Step 2: Use the type() function on each variable to print their data types.
print(my_integer, type(my_integer))
print(my_float, type(my_float))
print(my_string, type(my_string))
print(my_boolean, type(my_boolean))
print(my_list, type(my_list))

# Assign an integer a variable, try to modify the integer, and then reassess the variable to show that the original integer remains unchanged.
number = 42
print("Original number:", number)

new_number = number + 1
print("Modified number:", new_number)
print("Original number is still the name:", number)

# Convert a string that represents a number into an integer, then back to a string to observe how Python handles these transformations.
our_number_string = '100'
our_integer = int(our_number_string)
print(our_integer, type(our_integer))

our_new_string = str(our_integer)
print(our_new_string, type(our_new_string))

# Convert various values, including empty and non-empty strings, zeros, non-zero numbers, and None, to see which convert to True and which to False.
print(bool("")) # Empty string
print(bool("Python")) # Non-empty string
print(bool(0)) # Zero
print(bool(1)) # Non-zero number
print(bool(None)) # None


