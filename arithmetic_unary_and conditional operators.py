# Arithmetic operators allow us to manipulate numerical data.

# Addition (+): Adds two operands
# Subtraction (-): Subtracts the second operand from the first.
# Multiplication (*): Multiplies two operands
# Division (/): Divides the first operand by the second operand, always resulting in a float.
# Floor Division (///): Divides the first operand by the second and rounds down to the nearest integer.
# Modulo (%): Returns the remainder of the division of the first operand by the second.
# Exponentiation (**): Raises the first operand to the power of the second.

# FLOATING-POINT VS INTEGER DIVISION
# Floating-point division always returns a float, even if the operands are integers. This ensures precise calculations involving fractions or decimals.
# Integer division returns the floor of the division result, discarding any fractional part. This is useful when we specifically need an integer result, such as in cases where we are dividing indivisible entities or when we want to perform 
# integer arithmetic without introducing fractions.

# HANDLING COMMON ERRORS
# One common error is division by zero. Python will raise a ZeroDivisionError exception. 
# To handle this, we can use the try-except block.  

# UNARY OPERATORS
# Unary operators are special operators that perform operations on a single operand. Instead of using (++) and (--), Python uses unary plus (+) and unary minus (-).

# When applied to a positive value, unary plus (+) has no effect and the value remains unchanged. When applied to a negative value, the operator reverses the sign, making the value positive.
# When the unary minus (-) operator is applied to a positive value, it negates the value, making it negative. When applied to a negative value, it reverses the sign, making the value positive.

# these operators do not modify the original value. They return a new value with the appropriate sign.

# Although Python does not have built-in increment and decrement operators, we can achieve similar functionality using the += and =+ operators in combination with the value 1.

count = 5
count += 1
# After executing these lines, the value of count is 6.

count = 5
count -= 1
# After executing these lines, the value of count is 4.

# When using unary operators or increment/decrement operations, it is important to consider the mutability of the data types being operated on.
# Immutable types, such as integers, floats, and strings, can not be modified directly. When we perform an operation like += 1 or -= 1 on am immutable type, a new object is created with the updated value, and the original object remains unchanged.

x = 5
y = x
x += 1
print(x) # Output: 6
print(y) # Output: 5

# Mutable types, such as lists and dictionaries, can be modified directly. 

my_list = [1, 2, 3]
my_list[0] += 1
print(my_list) # Output: [2, 2, 3]

# CONDITIONAL OPERATORS
# Conditional operators in Python are essential for comparing values and making decisions based on those comparisons.

# Equal To (==): Checks if two values are equal.
# Not Equal To (!=): Checks if two values are not equal.
# Less Than (<): Checks if the left operand is less than the right operand.
# Greater Than (>): Checks if the left operand is greater than the right operand.
# Less Than or Equal To (<=): Checks if the left operand is less than or equal to the right operand.
# Greater Than or Equal to (>=): Checks if the left operand is greater than or equal to the right operand.

# These operators compare the values on either side and return a Boolean result (True or False) based on the outcome of the operation.


# Boolean values determine which block of code will be executed based on the truthiness of the condition. In conditional statements,s uch as if, elif, and else, the code block associated with a True condition is executed, while the code
# block associated with a False condition is skipped.


# Python provides logical operators (and, or, not) that allow us to combine conditions.
# The and operator returns True if both conditions are True.
# The or operator returns True if at least one of the conditions is True.
# The not operator negates the boolean value, return True if the condition is False, and vice versa.

# Python uses short-circuit evaluation when evaluating logical expressions. Short-circuiting means that it stops evaluating the remaining conditions as soon as the result of the expression can be determined. 
# If the first condition is False, Python will skip the second condition, determine the expression is False, and skip the code block.

