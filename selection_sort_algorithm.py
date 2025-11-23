# Selection Sort sorts an array by repeatedly finding the minimum or maximum element from the unsorted section and moving it to the end of the sorted section.
# We achieve this through a two-loop system: the outer loop gradually extends the sorted section by one element at a time, and the inner loop searches for and identifies the smallest or largest element in the unsorted part of the array. 
# After each complete pass of the inner loop, the identified element is swapped with the first element of the unsorted section.

# Pseudo-code
# To perform selection sort on a list:
# 1. Define a function called selection_sort that takes a parameter:
# - a list (arr)
# 2. Loop through each index i from 0 to the length of arr - 1:
# - Initialize min_index to i.
# - Loop through each index j from i+1 to the length of arr:
# - If arr[min_index] is greater than arr[j]:
# - Set min_index to j.
# - Swap arr[i] and arr[min_index].
# 3. Return the sorted list (arr).

# Selection Sort is most effective for small datasets or when memory write operations are a factor. This is because, regardless of the state of the array, selection sort will always perform the same number of comparisons and thus
# has a consistent execution time. However, due to its O(n^2) time complexity, selection sort becomes inefficient for larger datasets compared to more advanced sorting algorithms like Quick Sort or Merge Sort.

# This algorithm can be an ideal choice when sorting a small list of items, such as a list of names in a classroom or a handful of scores in a game. Its simplicity and the low overhead make it easy to implement and understand, 
# which is particularly useful in educational contexts or embedded systems with limited computational resources.

# Implement and Debug Selection Sort

# Pseudo-code
# 1. Define a function called selection_sort that takes a parameter:
# - a list (arr)
# 2. Traverse through all elements of the list using a loop from 0 to the
# length of arr - 1:
# - Initialize min_index to the current index i.
# - Loop through each index j from i + 1 to the length of arr:
# - If the element at min_index is greater than the element at j:
# - Set min_index to j.
# - Swap the element at index i with the element at min_index.
# 3. Return the sorted list (arr).


# Common Programming Errors in Selection Sort
# When implementing Selection Sort, we might encounter several common programming errors, such as off-by-one errors, incorrect minimum value identification, and errors in swapping logic. 
# To effectively debug issues, we can use print statements to monitor the array's state after each iteration, check our loop bounds to ensure all elements are compared correctly, and manually trace the algorithm with a small sample
# list to spot deviations from expected behavior.

# Off-by-one Error: May skip an element for comparison or attempt to access out-of-bounds.
# Check loop bounds; use print statements for verification.

# Incorrect Minimum Identification: Leads to an incorrect sort order because the wrong minimum is selected. 
# Manually trace with a small example; print array states.

# Swapping Logic Error: Incorrectly swaps elements, failing to place them in the correct position.
# Verify swap logic with print statements; trace through each swap


# Analyze and Compare Selection Sort's Performance
# Selection Sort has a time complexity of O(n^2) in the average and worst-case scenario. This quadratic time complexity arises because, for each element in the array, the algorithm scans the remaining elements to find the minimum 
# (or maximum) value, which involves a nested loop structure. Despite this seemingly inefficient time complexity, Selection Sort does not require additional memory beyond what is needed for the original array,
# giving it a space complexity of O(1), which means it's very efficient in terms of memory usage. 
# Ex: Consider sorting an array of 5 elements. In the worst case, Selection Sort would perform approximately (5 - 1) + (4 - 1) + (3 - 1) + (2 - 1) = 10 comparisons, demonstrating the O(n^2) time complexity.
 
# When we examine the performance of Selection Sort relative to Bubble Sort, both algorithms share the O(n^2) time complexity typical of more straightforward sorting methods. However, their operation approaches are quite different.
# Bubble Sort involves repeatedly comparing and swapping adjacent elements, potentially making it slower in practice compared to Selection Sort, which strategically minimize the number of swaps. This gives Selection Sort an edge,
# especially in situations where writing data is costlier than reading data.
# Ex: Consider sorting an array of 1,000 elements. While both Selection and Bubble Sort would require considerable time to complete due to their quadratic time complexities, Selection Sort might perform slightly better due to its
# reduced number of swaps. This applies to small datasets; for larger datasets, other algorithms would be more efficient.

# Optimize Selection Sort



