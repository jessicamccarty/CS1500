import time
import timeit
import sys
import random

# Write a linear search function: Begin with a simple linear search algorithm which possess linear time complexity O9n).

# Pseudo-code:
# To implement a linear search function:
# 1. Define a function called linear_search that takes two parameters:
# - a list (data)
# - a target element (target)
# 2. Inside the function:
# - Loop through a range of numbers from 0 to the length of data - 1 using
# a variable i:
# - If the element at data[i] is equal to the target:
# - Return True.
# - If the loop completes without finding the target, return False.
# 3. Test the function:
# - Define a list called data_list with values [1, 2, 3, 4, 5].
# - Define a variable called target_element and assign it the value 3 (or
# any other value to test different cases).
# - Call linear_search with data_list and target_element as arguments and
# store the result in a variable called result.
# - Print "Target found:" followed by the value of result.

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Test the function
data_list = [1, 2, 3, 4, 5]
target_element = 3 # Edit this value to test different cases
result = linear_search(data_list, target_element)
print("Target found:", result)


# Measure Execution Time: Utilize Python's timeit module to measure the execution time of the linear search function with varying input sizes.

# Pseudo-code:
# To measure the execution time of a linear search function using the
# timeit module:
# 1. Define the linear_search function:
# - The function takes two parameters:
# - a list (data)
# - a target element (target)
# - Loop through a range of numbers from 0 to the length of data - 1 using
# a variable i:
# - If the element at data[i] is equal to the target:
# - Return True.
# - If the loop completes without finding the target, return False.
# 2. Create a setup code string to ensure linear_search is in scope:
# - Import the linear_search function from the main module.
# - Import the random module.
# - Create a list called data with values ranging from 0 to 9999.
# - Select a random element from data and assign it to a variable called
# target.
# 3. Create a statement string to time:
# - Call the linear_search function with data and target as arguments.
# 4. Use the timeit module to measure the execution time:
# - Call timeit.repeat with the setup code, statement, repeat=3, and
# number=1000 to measure the execution time multiple times.
# - Store the results in a variable called times.
# 5. Print the minimum execution time:
# - Print "Linear search time:" followed by the minimum value in times and
# "seconds".

# Setup code to ensure linear_search is in scope
setup_code = "from __main__ import linear_search; import random; data = list(range(10000)); target = random.choice(data)"

# Statement to time
stmt = "linear_search(data, target)"

# Measure execution time
times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=1000)

# Print minimum execution time
print(f"Linear search time: {min(times)} seconds.")


# Analyzing Space Complexity

# Recursive Fibonacci Function: Write a recursive function to calculate Fibonacci numbers, a common example with significant space complexity due to recursion.

# Pseudo-code
# To implement a recursive Fibonacci function:
# 1. Define a function called fibonacci that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Check if n is less than or equal to 1:
# - If true, return n.
# - Otherwise:
# - Return the sum of calling fibonacci with n-1 and fibonacci with n-2.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

# Measure the Space Complexity: Measure the space complexity of the recursive Fibonacci function by analyzing the memory usage of each call stack and the total memory required to store intermediate results

# Pseudo-code
# To measure the space complexity of the recursive Fibonacci function:
# 1. Define a function called fibonacci_recursive that takes two parameters:
# - an integer (n)
# - an integer (depth) with a default value of 0
# 2. Inside the function:
# - Check if n is less than or equal to 1:
# - If true, return n.
# - Otherwise:
# - Call fibonacci_recursive with n-1 and depth+1, and store the result
# in a variable called left.
# - Call fibonacci_recursive with n-2 and depth+1, and store the result
# in a variable called right.
# - Calculate the sum of left and right, and store it in a variable
# called result.
# - If depth is 0 (initial call):
# - Print the maximum recursive depth.
# - Estimate the total memory for recursion by multiplying the size of
# result by 2 raised to the power of depth, and print the estimated memory in
# bytes.
# - Return the result.
# 3. Calculate the 10th Fibonacci number:
# - Call fibonacci_recursive with n = 10 and store the result in a
# variable called fib_number.
# - Print the 10th Fibonacci number along with the value of fib_number

def fibonacci_recursive(n, depth=0):
    if n <= 1:
        return n
    else:
        left = fibonacci_recursive(n-1, depth+1)
        right = fibonacci_recursive(n-2, depth+1)
        result = left + right
        if depth == 0: # Only print on the intial call
            print(f"Maximum recursive depth: {depth}.")
            print(f"Estimated total memory for recursion (bytes)", sys.getsizeof(result) * ( 2 ** depth))
        return result
    
# Calculate the 10th Fibonacci number
fib_number = fibonacci_recursive(10)
print("10th Fibonacci number:", fib_number)


# Balancing Time and Space Complexity

# Optimize the Algorithm: Optimize the Fibonacci function using an iterative approach, which maintains linear time complexity O(n) but reduces space complexity to constant O(1).

# Pseudo-code
# To implement an optimized Fibonacci function using an iterative approach:
# 1. Define a function called fibonacci_iterative that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Initialize two variables a and b to 0 and 1, respectively.
# - Loop through a range of numbers from 0 to n-1 using a variable i:
# - In each iteration, update a and b as follows:
# - Assign the value of b to a.
# - Assign the sum of a and b to b.
# - After the loop, return the value of a.

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

# Measure and Compare Performance: Measure the performance of both the original and optimized versions to see the impact of our optimization.

# Pseudo-code
# To measure and compare the performance of the original recursive and
# optimized iterative Fibonacci functions:
# 1. Measure the performance of the original recursive function:
# - Create a setup code string to ensure the fibonacci function is in
# scope by importing it from the main module.
# - Create a statement string to call the fibonacci function with the
# argument 20.
# - Use the timeit module to measure the execution time:
# - Call timeit.repeat with the setup code, statement, repeat=3, and
# number=1 to measure the execution time multiple times.
# - Store the minimum execution time in a variable called
# time_recursive.
# 2. Measure the performance of the optimized iterative function:
# - Create a setup code string to ensure the fibonacci_iterative function
# is in scope by importing it from the main module.
# - Create a statement string to call the fibonacci_iterative function
# with the argument 20.
# - Use the timeit module to measure the execution time:
# - Call timeit.repeat with the setup code, statement, repeat=3, and
# number=1 to measure the execution time multiple times.
# - Store the minimum execution time in a variable called
# time_iterative.
# 3. Print the execution times:
# - Print "Recursive Fibonacci time:" followed by the value of
# time_recursive and "seconds".
# - Print "Iterative Fibonacci time:" followed by the value of
# time_iterative and "seconds".

# Measure the original recursive function
setup_code_recursive = "from __main__ import fibonacci"
stmt_recursive = "fibonacci(20)"
time_recursive = min(timeit.repeat(setup=setup_code_recursive, stmt=stmt_recursive, repeat=3, number=1))

# Measure the optimized iterative function
setup_code_iterative = "from __main__ import fibonacci_iterative"
stmt_iterative = "fibonacci_iterative(20)"
time_iterative = min(timeit.repeat(setup=setup_code_iterative, stmt=stmt_iterative, repeat=3, number=1))


print(f"Recursive Fibonacci time: {time_recursive} seconds.")
print(f"Iterative Fibonacci time: {time_iterative} seconds.")