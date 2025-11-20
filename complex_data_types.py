from enum import Enum
from array import array

# Python's complex data types, such as lists, tuples, arrays, dictionaries, sets, bytes, byte arrays, and enumeration types (Enum), greatly broaden its capabilities.
# They allow for orderly data organization, efficient storage and retrieval, precise data manipulation, and more readable code by limiting variables to specific values. 

# We use sequence types, like lists, tuples, and arrays to store and organize items in a specific order. This order lets us access elements by their position in the sequences, which starts at zero.
# We often use lists and tuples because they can hold different types of items.
# The difference between them is that we can change lists after creating them, but tuples remain the same, which is great for data that shouldn't change over time.

# Lists are versatile and widely used. We define lists with square brackets [ ], and can fill them with a mix of item types, even including other lists.
# Lists are perfect for when data collection needs to adjust by adding, removing, or altering items. They also support various operations, making them incredibly flexible.

# Tuples, like lists, contain a mix of item types but are immutable. This makes tuples ideal for storing dta that must stay constant, like database keys or fixed data sets.

# Arrays are more specialized, designed for efficiently storing numbers of the same type. We need to import a module to use arrays, but they are worth it for large collections of numerical data because
# they save space and improve performance. However, they are less flexible than lists because they only hold one data type.

my_list = [1, "Hello", [1, 2, 3], True]
my_tuple_coordinates = (10.0, 20.0)
int_array = array('i', [1, 2, 3, 4, 5]) 

# In Python, the dictionary is the foundational mapping type. Maps allow us to efficiently retrieve, add, or delete data through unique and immutable keys. Dictionaries excel in representing complex data 
# relationships and streamlining data access.

# We often use dictionaries(dict) to organize our data into key-value pairs. This is like a map, where each unique, unchangeable key leads us to its corresponding value. Values can be of any type and appear
# more than once, but every key must be one of a kind and immutable, like a string or number.

# We define dictionaries with curly braces {}, separating each key from its value with a colon. 
person_info = {"name" : "John", "age": 30}
# adding/updating:
person_info["email"] = "john@exmaple.com"

# Because of their speed and simplicity, we can use dictionaries for counting items, organizing complex information, or creating data mappings. They are mutable, so we can add, change, or remove key-value
# pairs anytime, making our data dynamic and flexible. Python also provides tools like get(), keys(), values(), and items() to work with dictionaries efficiently.
print(person_info.get("age"))
# remove: del person_info["email"]

# Sets(set) are an unordered collection of unique elements. They are mutable, which allows us to add or remove elements after they have been created. You define a set by enclosing its elements within curly 
# braces {} or by using the set() constructor. Sets are unordered and we use them when we need each element to be unique while the sequence of elements doesn't matter.
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)

# Enumeration refers to the act of naming or listing things one by one. It involves the process of specifying individual elements from a group or collection in a systematic and orderly sequence.
# In Python, enumerations are used to assign names to constant values. The enumeration Enum type comes from the Enum class in the enum module. They help us make our code more readable and maintainable
# by providing a clear and concise way to handle sets of related constants.

# We use enumerations(Enum) to group symbolic names (members) tied to unique, constant values into a single, coherent entity. This approach allows us to compare these members by their name.
# Each member within an Enum is identified by a name and associated with a value, which is often an integer but can be other types as well.
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# In Python, we use binary sequences to work with bytes, the basic units of digital information composed of 1s and 0s. There are two main kinds: bytes, which we can't change once created, and bytearray, which we can modify.
# These types are important when we are dealing with things like file contents and network data.

# We define the bytes type by adding a b prefix to a string literal or by transforming a list of integers into bytes using the bytes() constructor. In this constructor, each integer stands for a byte in the sequence and falls within the range of
# 0 to 255. The fact that bytes are unchangeable makes the perfect for representing constants in our programs, especially when we're dealing with fixed sequences of byte data.
greeting = b'hello'
bytes_from_list = bytes([72, 101, 108, 108, 111])

# In contrast, the bytearray type is much more flexible, allowing us to dynamically append, remove, or modify elements. This flexibility makes it ideal for our read-write operations on byte data. 
# We can create a byte array using the bytearray() constructor.
ba = bytearray(b'hiya')
ba[0] = 72
print(ba)

ba.append(33)
# ba.pop() Removes last element
print(ba)
