# To implement and observe the performance of expensive operations inside
# loops:
# 1. Define a function called expensive_operations that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Record the current time in a variable called start_time.
# - Loop through a range of numbers from 0 to n-1 using a variable i:
# - For each i, call a function named some_expensive_function with i as
# the argument and store the result in a variable called result.
# - Print the value of result.
# - After the loop, record the current time in a variable called end_time.
# - Calculate the execution time by subtracting start_time from end_time.
# - Print the execution time along with the value of n.
# 3. Define a function called some_expensive_function that takes a parameter:
# - an integer (i)
# 4. Inside the function:
# - Simulate an expensive operation by delaying for 10 milliseconds using
# time.sleep(0.01).
# - Return the square of i.
# 5. Test the expensive_operations function with different values of n:
# - Call expensive_operations with n = 10.
# - Call expensive_operations with n = 20.

import time

def expensive_operations(n):
    start_time = time.time()
    for i in range(n):
        result = some_expensive_function(i)
        print(result)
    end_time = time.time()
    print("Execution Time for n =", n, ":", end_time - start_time, "seconds.")

def some_expensive_function(i):
    # Simulate an expensive operation
    time.sleep(0.01) # Delays for 10 milliseconds
    return i * i

# Test the function with different values of n
# expensive_operations(10)
# expensive_operations(20)

expensive_operations(n)