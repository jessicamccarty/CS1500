# To implement and observe the performance of complex operations inside
# nested loops:
# 1. Define a function called complex_operations that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Record the current time in a variable called start_time.
# - Loop through a range of numbers from 0 to n-1 using a variable i:
# - For each i, loop through a range of numbers from 0 to i-1 using a
# variable j:
# - Print the values of i and j.
# - After the nested loops, record the current time in a variable called
# end_time.
# - Calculate the execution time by subtracting start_time from end_time.
# - Print the execution time along with the value of n.
# 3. Test the function with different values of n:
# - Call complex_operations with n = 10.
# - Call complex_operations with n = 50.

import time

def complex_operations(n):
    start_time = time.time()
    for i in range(n):
        for j in range(i):
            print(i, j)
    end_time = time.time()
    print("Execution Time for n =", n, ":", end_time - start_time, "seconds.")

# Test function with different values of n
# complex_operations(10)
# complex_operations(50)

complex_operations(n)