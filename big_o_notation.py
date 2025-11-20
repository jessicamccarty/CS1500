# Big O Notation is a way to measure how well an algorithm performs, especially in the "worst-case scenario." 
# It illustrates how the time or space requirements of an algorithm increase as the size of the data it processes grows. 
# This growth is measured in terms of the input size, denoted as "n".

# One important aspect of Big O Notation is its role in understanding the scalability of algorithms. 
# Scalability refers to an algorithm's ability to maintain its efficiency and performance level as the size of the input data increases.

# Big O Notation:
# (f(n) = O(g(n))) if there exist constants (c) and (n0) such that (0 ≤0 f (n) ≤ c ⋅ g(n)) for all (n ≥ n0)

# (f(n) = O(g(n)))
# The function of (f(n)) is said to be Big O of (g(n)). This means that as the size of the input (n) increases, the growth rate of (f(n)) will be limited or bounded by the growth rate of (g(n)), multiplied by some constant. 
# Essentially, (g(n)) sets an upper limit on how fast (f(n)) can grow.

# if there exist constants (c) and (n0)
# For this relationship to hold true, there must be some specific numbers, named (c) and (n0), that make the equation work. (c) acts like a scaling factor or multiplier, and (n0) is the point from which this rule starts to apply.
# This means the rule doesn't necessarily apply when (n) is very small, but it must work for all larger values.

# such that (0 ≤0 f (n) ≤ c ⋅ g(n))
# This part specifies the actual condition that must be met: the value of (f(n)) must always be greater than or equal to zero and less than or equal to (c) times (g(n)). This means (f(n))'s values are squeezed within a range defined
# by zero and (c * g(n)), ensuring (f(n)) doesn't grow faster than (g(n)) times some constant.

# for all (n ≥ n0)
# This condition applies to all numbers (n) that are greater than or equal to (n0). It tells us that the rule about (f(n))'s growth being controlled by (g(n)) starts from (n0) and continues for all larger numbers.
# (n0) is the starting line beyond which the given rule must always be true.

# EXPLANATION OF BIG O NOTATIONS
# O(1) Constant Time: No matter the size of the data, the operation completes in the same time.
# O(log n) Logarithmic Time: As the data grows, the number of operations grows very slowly. Common in operations like binary search.
# O(n) Linear Time: The number of operations grows linearly with the size of the data.
# O(n log n) Linearithmic Time: More efficient than quadratic time but less efficient than linear time. Common in efficient sorting algorithms like merge sort and quick sort.
# O(n^2) Quadratic Time: The number of operations is proportional to the square of the size of the data. Typical for simple sorting algorithms like bubble sort and selection sort.
# O(2^n) Exponential Time: Operations grow exponentially with the data size. Often impractical for large data sets.


# Time Complexity Analysis is a method we use to determine how the execution time of an algorithm increases as the size of the input data grows. Analyzing time complexity help sus predict the performance limits of algorithms
# under different conditions. 
# EX: Linear search is O(n), time increases linearly with n

# Space Complexity Analysis is concerned with the total amount of memory an algorithm needs to run to completion. It is important for application performance, especially in environments with limited memory resources. 
# An example of optimizing for space is using an iterative version of the Fibonacci sequence calculation instead of a recursive one, significantly reducing the memory overhead.
# EX: Iterative Fibonacci is O(1), uses constant space



