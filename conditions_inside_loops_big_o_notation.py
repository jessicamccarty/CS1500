# To implement and observe the performance of a loop with conditions
# inside:
# 1. Define a function called condition_inside_loop that takes a parameter:
# - an integer (n)
# 2. Inside the function:
# - Record the current time in a variable called start_time.
# - Loop through a range of numbers from 0 to n-1 using a variable i:
# - For each i, check if i is divisible by 2 (i % 2 == 0):
# - If the condition is true, print the value of i.
# - After the loop, record the current time in a variable called end_time.
# - Calculate the execution time by subtracting start_time from end_time.
# - Print the execution time along with the value of n.
# 3. Test the function with different values of n:
# - Call condition_inside_loop with n = 10.
# - Call condition_inside_loop with n = 100.
# - Call condition_inside_loop with n = 1000.

import time

def condition_inside_loop(n):
    start_time = time.time()
    for i in range(n):
        if i % 2 == 0:
            print(i)
    end_time = time.time()
    print("Execution Time for n = ", n, ":", end_time - start_time, "seconds.")

# Test the function with different values of n
# condition_inside_loop(10)
# condition_inside_loop(100)
# condition_inside_loop(1000)

condition_inside_loop(n)
