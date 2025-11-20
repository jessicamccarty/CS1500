# Variables serve as containers to store data values that our program can manipulate. Data types provide us a way to represent forms of information.

# A variable by definition is a storage location in a computer's memory that is associated with a symbolic name, containing a known or unknown quantity of information referred to as a value.
# Variables are essential for more than just data storage; they enable developers to write flexible and dynamic code that can adapt over time and facilitate the creation of programs that interact with user input.

#  Declaring variables in Python is a straightforward process. The declaration happens automatically when we assign a value to a variable for the first time. Use the assignment operator (=) to link a variable name 
# on the left to a value on the right. 

# When naming variables in Python, there a few conventions that we must follow to make code readable and maintainable.
# 1. Variable names should be descriptive enough to make it clear what data they hold. Ex. user_age
# 2. They can include letters, digits, and underscores, but cannot start with a digit.
# 3. Python is case-sensitive which means userAge and userage are considered two distinct variables.
# 4. Avoid using reserved keywords, such as if, for, and while.

# Simple data types, also known as primitive data types, are the basic building blocks for data manipulation and define the kind of operations that can be preformed on data stored in variables.
# These include integers (int), floating-point numbers (float), string (str), and Booleans (bool). Python also includes NoneType with a single value None to represent the absence of a value.

# Integers(int) are whole numbers that can be positive, negative, or zero. They have no decimal point and can be of any length, limited only by memory of the system. Integers are commonly used for counting,
# iterations in loops, and anytime we need to represent countable, discrete quantities.

# Floating-point numbers(float) represent real numbers and are written with a decimal point dividing the integer and fractional parts. Floats can also be represented using scientific notation, with an "e" to
# indicate the power of 10. We use floating-point numbers when more precision is needed, such as calculations involving fractions or when representing measurements that are not whole numbers.
# Floats in Python are an approximation which can lead to precision issues in complex calculations.

# Complex numbers(complex) are used in fields like engineering, physics, and mathematics, especially for calculating the square roots of negative numbers. 
# A complex number consists of two parts: a real part and an imaginary part.
# The real part of the complex number can be found on the traditional number line. It represent the "real" aspect of the number, similar to the numbers we use in everyday math.
# The imaginary part of a complex number involves the square root of -1, which is represented by the symbol i in mathematics or j in engineering and Python programming.

# Decimals(decimal.Decimal) are a special data type in Python that offer decimal arithmetic suitable for accounting applications and high-precision applications. Unlike floating-point numbers, decimals have
# a user-defined precision which makes them more accurate. This is useful in financial calculations where exact decimal representation and precision are required.
# To use decimals, you must import the Decimal class from Python's decimal module.

# Fractions (fractions.Fraction) represent rational numbers as a numerator and a denominator, both integers. They are part of the Python fractions module and are used when exact divisions are need to be 
# preserved. We use fractions in situations where floating-point division might introduce unacceptable rounding errors, making them particularly valuable in mathematical and scientific computations where
# precision is crucial.

# Strings(str) are sequences of characters enclosed in quotes and are used extensively in Python for holding textual data, formatting information, and any scenario where human-readable text is necessary. 
# We can enclose strings in single quotes ('Hello') or double quotes ("Hello"), and Python treats both forms equally. Strings are immutable, which means once a string is created, it cannot be changed.

# Booleans(bool) represent one of two values: True or False. We can use Booleans to determine if a number is greater than another variable or if a variable is None. Beyond their simple True or False
# representation, Booleans are also treated as numeric types in Python, with True corresponding to 1 and False to 0, allowing them to be used in arithmetic operations.

# NoneType(None) is a special type in Python that has a single value, None. We use it to signify the absence of a value or a null value, instead of null. None is particularly useful when we need to create a
# variable but don't have an initial value for it or when a function does not explicitly return a value. It acts as a placeholder that can be checked in conditional statements. 

# Python is dynamically typed, which means the interpreter infers the type of an object at runtime. The type() function allows us to inspect and understand the type of variable we are working with.
# When we pass a given value or variable to the type() function, Python returns the class type of that value.
num = 42
print(type(num))

# In Python, declaring a variable happens the moment we assign a value to it. Problem often occur if we use == instead of =, or if we omit quotes around string values, leading to misidentification.
# Correct:
name = "John Does"
# Incorrect:
name == "John Does"
name = John Does # type: ignore

# Type mismatches arise when an operation expects a certain data type but receives another. These errors may not be evident until runtime.
# Incorrect concatenation leading to TypeError:
age = 25
message = "John is " + age + " years old."
# Correct approach with type conversion:
message = "John is " +str(age) + " years old."

