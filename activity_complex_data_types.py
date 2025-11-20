from enum import Enum
from array import array

# Create a list that contains a variety of data types including integers, strings, and another list.
mixed_list = [42, "Hello, world!", [1, 2, 3]]
print("Original list: ", mixed_list)

# Append a different type of element to this list, specifically a floating-point number.
mixed_list.append(3.14)
print("List After Appending: ", mixed_list)

# Remove an element from the list using the remove() method.
mixed_list.remove("Hello, world!")
print("List After Removal: ", mixed_list)

# Modify an element in the list. Change 42 to 100.
mixed_list[0] = 100
print("List After Modification: ", mixed_list)

# MANAGING A LIST OF MIXED ELEMENTS
# Create an initial list that contains a variety of data types: a string, an integer, and a list.
my_list = ["map", 38, ["compass", "water bottle"]]
print("Original list: ", my_list)

# Add a floating-point number representing the temperature 24.5 and a boolean value indicating it is not raining.
my_list.append(24.5) # Can only do 1 argument at a time
my_list.append(False)
print("List after appending: ", my_list)

# Remove the integer value from the list.
my_list.remove(38)
print("List after removal: ", my_list)

# Change the first element in the list from "map" to "GPS"
my_list[0] = "GPS"
print("List after modification: ", my_list)

# TUPLES
# Create a tuple that includes an integer, a string, and a list.
my_tuple = (10, "Python", [2, 4])
print("Original Tuple: ", my_tuple)

# Attempt to change one of the elements of the tuple
try:
    my_tuple[1] = "Attempted Change"
except TypeError as e: 
    print("Error", e)
    
# Iterate through the tuple and print each element.
for item in my_tuple:
    print("Tuple Item: ", item)

# Create a new tuple that contains a variety of data types: a string, an integer, and a list
new_tuple = ("book", 2023, ["pen", "notebook"])

# Attempt to modify the string element in the tuple from "book" to "eBook"
try:
    new_tuple[0] = "eBook" 
except TypeError as e:
    print("Error:", e)

# Iterate through the tuple
for item in new_tuple:
    print("Tuple item: ", item)


# ARRAYS
# Create an array that consists of integers
numeric_array = array('i', [10, 20, 30])
print("Original array: ", numeric_array)

# Append an element to this array
numeric_array.append(40)
print("Array after appending: ", numeric_array)

# Remove the element 20 from the array
numeric_array.remove(20)
print("Array after removal: ", numeric_array)

# Modify the last element from 40 to 50
numeric_array[-1] = 50
print("Array after modification: ", numeric_array)

# Create a new array containing integers
new_array = array('i', [50, 100, 150])
print("Original array: ", new_array)

# Add the integer 200 to the array
new_array.append(200)
print("Array after appending: ", new_array)

# Change the first element in the array from 50 to 55
new_array[0] = 55
print("Array after modification: ", new_array)


# DICTIONARIES
# Create a dictionary with a variety of key types including a string, an integer, and a tuple, and corresponding values.
mixed_dict = {"name": "Alice", 42: "The Answer", (0, 1): "Tuple Key"}
print("Original Dictionary: ", mixed_dict)

# Add a new key-value pair with a floating-point number as a key.
mixed_dict[3.14] = "Pi"
print("Dictionary after appending: ", mixed_dict)

# Remove a key-value pair from the dictionary. Remove the integer key 42.
del mixed_dict[42]
print("Dictionary after removal: ", mixed_dict)

# Change the value of the key name from "Alice" to "Bob"
mixed_dict["name"] = "Bob"
print("Dictionary after modification: ", mixed_dict)

# Create a new dictionary with a variety of key types including a string, an integer, and a tuple, and corresponding values.
new_dict = {"author": "Alice Walker", 2023: ["January", "February", "March"], ("latitude", "longitude"): "34.0522° N, 118.2437° W"}
print("Original dictionary", new_dict)

# Add a new key-value pair to the dictionary
new_dict[3.14159] = True
print("Dictionary after appending: ", new_dict)

# Remove the tuple key from the dictionary.
del new_dict["latitude", "longitude"]
print("Dictionary after removal: ", new_dict)

# change the value associated with the key "author" from "Alice Walker" to "Maya Angelou"
new_dict["author"] = "Maya Angelou"
print("Dictionary after modification: ", new_dict)


# SET OPERATIONS
# Create an initial set of numbers
number_set = {1, 2, 3, 4, 5}
print("Initial set:", number_set)

# Add a new item to the set
number_set.add(6)
print("After adding 6:", number_set)

# Attempt to add a duplicate to demonstrate the uniqueness property of sets
number_set.add(3)
print("After trying to add 3 again:", number_set)

# Remove an item from the set
number_set.remove(4)
print("After removing 4:", number_set)

# Examine the final state of the set
print("Final set:", number_set)
print("Number of elements:", len(number_set))
print("Is 3 in the set?", 3 in number_set)
print("Is 4 in the set?", 4 in number_set)

# Create a set called languages
language_set = {"Python", "JavaScript", "Java", "C++"}
print("Initial set:", language_set)

# Add Ruby and Python to the language set.
language_set.add("Ruby")
language_set.add("Python")
print("Set after adding:", language_set)

# Remove C++ from the set
language_set.remove("C++")
print("Set after removing:", language_set)

# Examine the set
print("Final set:", language_set)
print("Number of elements:", language_set)
print("Is Python in the set?", "Python" in language_set)
print("Is C++ in the set?", "C++" in language_set)


# ENUMERATIONS
# Define an Enum for the days of the week
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print("Enumeration for Day of the Week:", list(Weekday))

# Use the enumeration to determine if a day is a weekday or weekend then display an appropriate message.
def check_day(day):
    if day in (Weekday.SATURDAY, Weekday.SUNDAY):
        return f"{day.name} is a weekend."
    else:
        return f"{day.name} is a weekday."
    
current_day = Weekday.WEDNESDAY
print(check_day(current_day))

# Highlight a specific day and print something special about it.
special_day = Weekday.FRIDAY
print(f"Ah, {special_day.name}, the gateway to the weekend.")

# Create an enumeration named Season that includes four seasons: Spring, Summer, Autumn, and Winter
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

# Append the elements by creating a method to print a custom greeting for each season.
def check_season(season):
    if season == (Season.SUMMER):
        return f"{season.name} is too hot!"
    if season == (Season.WINTER):
        return f"{season.name} is too cold!"
    else:
        return f"{season.name} is just right!"
    
current_season = Season.WINTER
print(check_season(current_season))
next_season = Season.SUMMER
print(check_season(next_season))
final_season = Season.SPRING
print(check_season(final_season))

