# To implement and observe the performance of a simple loop:
# 1. Import the necessary module:
# - time
# 2. Define a function called simple_loop that takes a parameter:
# - an integer (n)
# 3. Inside the function:
# - Record the current time in a variable called start_time.
# - Loop through a range of numbers from 0 to n-1:
# - For each number i in the range, print the value of i.
# - After the loop, record the current time in a variable called end_time.
# - Calculate the execution time by subtracting start_time from end_time.
# - Print the execution time along with the value of n.
# 4. Test the function with different values of n:
# - Call simple_loop with n = 10.
# - Call simple_loop with n = 100.
# - Call simple_loop with n = 1000.


import time

def simple_loop(n):
    start_time = time.time()
    for i in range(n):
        print(i)
    end_time = time.time()
    print("Execution Time for n =", n, ":", end_time - start_time, "seconds.")
    
# Test the function with different values of n
# simple_loop(10)
# simple_loop(100)
# simple_loop(1000)


simple_loop(n)
