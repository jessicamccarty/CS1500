# To implement and observe the performance of nested loops:
# 1. Define a function called nested_loops that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Record the current time in a variable called start_time.
# - Loop through a range of numbers from 0 to n-1 using a variable i:
# - For each i, loop through another range of numbers from 0 to n-1
# using a variable j:
# - Print the values of i and j.
# - After the nested loops, record the current time in a variable called
# end_time.
# - Calculate the execution time by subtracting start_time from end_time.
# - Print the execution time along with the value of n.
# 3. Test the function with different values of n:
# - Call nested_loops with n = 10.
# - Call nested_loops with n = 20.

import time

def nested_loops(n):
    start_time = time.time()
    for i in range(n):
        for j in range(n):
            print(i, j)
    end_time = time.time()
    print("Execution Time for n =", n, ":", end_time - start_time, "seconds.")


# Test the function with different values of n
# nested_loops(10)
# nested_loops(100)

nested_loops(n)