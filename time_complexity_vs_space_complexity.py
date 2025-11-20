# Time complexity refers to the computational time an algorithm takes to complete as a function of the length of the input. It gives us an idea of the growth rate of the algorithm's running time. 
# EX: A linear search algorithm that checks each item in a list one by one until a match is found has a time complexity of O(n), where n represents the number of items in the list.
# This means that the time it takes to complete the search grows linearly with the size of the input.

# To perform a linear search in a list:
# 1. Define a function called linear_search that takes two parameters:
# - a list (myList)
# - an item to search for (item)
# 2. Loop through each index i from 0 to the length of my List - 1:
# - If myList(i) is equal to item:
# - Return i (the index of the item)
# If the loop ends without finding the item:
# - Return -1 (item not found)


# Space complexity deals with the amount of memory space required by an algorithm to run to completion. It helps us understand how much memory an algorithm needs in relation to the size of its input.
# EX: A sorting algorithm that sorts the items in place without requiring additional storage space has a space complexity of O(1).
# This means that the space required does not increase with the size of the input.

# To perform a bubble sort on a list:
# 1. Define a function called bubble_sort that takes a parameter:
# - a list (myList)
# 2. Loop through each index i from the length of myList - 1 down to 1:
# - Loop through each index j from 0 to i - 1:
# - If myList[j] is greater than myList[j + 1]:
# - Swap myList[j] and myList[j + 1]
# Return the sorted list (myList)


# The bubble_sort function has a space complexity of O(1), which means it uses a constant amount of extra memory space regardless of how many items are in the list. This is because all the sorting happens in the original list
# without needing additional storage space.


# Big O Notation is used to express the upper bound of an algorithm's time or space complexity. It focuses on the worst-case scenario. It allows us to abstract away constraints and lower-order terms to concentrate on the part of the
# complexity that grows the fastest as the input size increases. This abstraction makes it easier to compare the efficiency of different algorithms.
# EX: When comparing Quick Sort and Bubble Sort, Quick Sort generally has a time complexity of O(n log n) making it more efficient than Bubble Sort, which has a time complexity of O(n^2) for large inputs.


# There will always be a trade-off between time complexity and space complexity with algorithms.
# EX: An algorithm with O(1) space complexity might have O(n^2) time complexity making it slow for large datasets. Conversely, an algorithm with O(n log n) time complexity might require O(n) space, making it memory-intensive.


# The Fibonacci Sequence is a series of numbers where each number is the sumer of the two numbers before it, usually starting with 0 and 1.
# [ F(n) = F(n-1) + F(n-2)] with initial conditions [ F(0) = 0, \quad F(1) = 1 ]


# Recursion is a programming technique where a function calls itself in order to solve smaller instances of the same problem. It's often used when a problem can naturally be divided into similar sub-problems.
# Recursion can lead to precise code, but can also be memory-intensive and slower due to overhead of multiple function calls and the maintenance of the call stack, which keeps track of the function calls.


# Iterative Approach
# In the iterative approach to calculating Fibonacci numbers, the function initializes two variables to the first two Fibonacci numbers and iterates n times, updating these variables to the next two Fibonacci numbers each time.
# The value of a ends up holding the nth Fibonacci number, which is returned.
# The space complexity is O(1) because it uses  fixed amount of space regardless of n.
# The time complexity is O(n) because it iterates through n operations to compute the nth Fibonacci number.

# 1. Define a function called fibonacci_iterative that takes a parameter:
# - an integer (n)
# 2. Initialize two variables, a and b, to 0 and 1, respectively (the first two Fibonacci numbers)
# 3. Loop n times:
# - Update a and b to the next two Fibonacci numbers.
# 4. Return the value of a, which now holds the nth Fibonacci number.


# Recursive Approach
# In the recursive approach to calculating Fibonacci numbers, the function checks if n is 0 or 1 and returns n if true, as these are the base cases. 
# For other values, it recursively calls itself to compute the two preceding Fibonacci numbers and returns their sum.
# The space complexity is higher due to the call stack used in recursive calls, which can grow substantially with n.
# The time complexity can be exponential, O(2^n), because it recalculates the same Fibonacci numbers multiple times.

# 1. Define a function called fibonacci_recursive that takes a parameter:
# - an integer (n)
# 2. If n is less than or equal to 1:
# - Return n (base case)
# 3. Otherwise:
# - Return the sum of fibonacci_recursive(n - 1) and fibonacci_recursive (n - 2) 


# Apply Time and Space Complexity for Efficiency
# 1. Define Requirements and Constraints:
# Suppose we're developing a feature in a text editing application that needs to sort words or letters frequently input by the user alphabetically. The primary constraint is a quick response time and minimal memory usage
# to keep the app responsive on devices with limited resources.
# 2. Select Appropriate Algorithms:
# We chose the insertion sort algorithm for its simplicity and its ability to perform well with small to medium-sized datasets, which is typical in user input scenarios.
# 3. Analyze Initial Complexity:
# Insertion sort has a time complexity of (O(n^2)) and a space complexity of (O(1)) when sorting in place. Given our constraints, the linear space complexity is ideal, but we need to ensure the quadratic time complexity
# won't hinder performance for expected input sizes.
# 4. Implement and Test:
# Implement the insertion sort to organize characters within strings:
# 4a. Define a function called insertion_sort_string that takes a parameter:
# - a string (s)
# 4b. Convert the string to a list of characters (arr) for manipulation.
# 4c. Loop through each index i from 1 to the length of arr -1:
# - Set key to arr[i]
# - Initialize j to i - 1
# - While j is greater than or equal to 0 and arr[j] is greater than key:
# - Set arr[j + 1] to arr[j
# - Decrement j by 1
# - Set arr[j + 1] to key.
# 4d. Convert the sorted list of characters back into a string and return it.
# This approach is space-efficient as it modifies the string in place, only temporarily extracting each character to be inserted.
# It efficiently manages space by requiring no additional memory beyond what is used to store the string itself, aside from the temporary variable key.
# 5. Optimize:
# Observe the performance during testing. If the sorting becomes a bottleneck, consider optimizing by switching to a more efficient algorithm or implement techniques like memoization where applicable to improve repeated operations.
# 6. Iterate:
# Test with varying sizes of inputs and under different system conditions to ensure consistency of performance. Refine the algorithm based on test results, possibly tweaking how characters are compared and moved.
# 7. Document and Deploy:
# Document the final algorithm, noting any conditions under which it switch strategies (ex. for larger datasets). Deploy it in the text editing application and monitor its performance, particularly looking at scenarios with extensive
# user interaction.

# Memoization: An optimization technique that saves the results of expensive function calls to avoid repeating the same calculations.
# Ex: Using a dictionary to store Fibonacci numbers as they are calculated to prevent redundant computations.
