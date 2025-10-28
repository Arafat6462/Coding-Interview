# variables are dynamically typed
# no need to declare variable type
# variable types are inferred at runtime
n = "hello"
print(n)

n = 10
print(n)



# multiple assignment in one line
a, b, c = .012, "hello", False
print(a, b, c)



# Incrementing a variable
n = n + 1 # Good
n += 1    # Good
# n++  # not valid in python



# None is null (absence of value)
n = 3
n = None
print(n)



# if statement don't need parentheses or curly braces
# python uses indentation to define blocks of code
if n is None:
    print("n is None")



# Parentheses needed in multi-line expressions
# and = &&
# or = ||
# not = !
if ((n is None or n == 3) 
    and not (n == 4)):
    print("n is None or n is 3 and n is not 4")



# While loops are simple
i = 0
while i < 5:
    print(i)
    i += 1



# For loops using range()
# Basic for loop: iterates from 0 to 4
for i in range(5):
    print(i)

# For loop with custom start and end: iterates from 2 to 4
for i in range(2, 5):
    print(i)

# For loop with step: iterates from 2 to 8, stepping by 2
for i in range(2, 10, 2):
    print(i)

# For loop in reverse: iterates from 10 down to 3, stepping by -1
for i in range(10, 2, -1):
    print(i)

# For loop in reverse with step: iterates from 5 down to 1, stepping by -2
for i in range(5, 0, -2):
    print(i)




# Division (/) always returns a float
print(5 / 2)  # 2.5
print(8 / 4)  # 2.0

# Floor division (//) returns the largest integer less than or equal to the result
print(5 // 2) # 2

# Floor division with negative numbers rounds down to the next lowest integer
print(3 // 2)   # 1
print(-3 // 2)  # -2

# Be careful with negative numbers and floor division
# -3 / 2 is -1.5, floor division rounds down to -2
# but int(-3 / 2) truncates towards zero to -1
# Casting to int truncates towards zero (not always the same as floor division)
print(int(-3 / 2)) # -1, here first does true division then truncates towards zero



# Modulus operator (%) returns the remainder of division
print(10 % 3)      # Remainder of 10 divided by 3 is 1

# Exception for negative numbers
print(-10 % 3)     # In Python, modulus keeps the sign of the divisor, so -10 % 3 is 2

import math
print(math.fmod(-10, 3))  # Using math.fmod gives -1.0, which keeps the sign of the dividend

# More math helpers
print(abs(-5))        # Absolute value
print(pow(2, 3))     # 2 raised to the power of 3
print(math.sqrt(16)) # Square root
print(round(34.6))    # Rounds to nearest integer
print(round(3.14159, 2)) # Rounds to 2 decimal places
print(math.ceil(3.2))  # Rounds up to nearest integer
print(math.floor(3.8)) # Rounds down to nearest integer
print(math.log(100, 10)) # Log base 10 of 100
print(math.log2(8))     # Log base 2 of 8


# max and min
print(max(3, 5))  # 5
print(min(3, 5))  # 3
print(float('inf'))  # Positive infinity
print(float('-inf')) # Negative infinity

# Python numbers ate infinite so no overflow errors
print(2**1000)  # Very large number

# But still less than infinity
print(2**1000 < float('inf'))  # True



# Arrays (called lists in python). most common data structure next to hashmaps (dicts)
arr = [1,2,3]
print(arr) # [1, 2, 3]

# List can be used as stacks, queues, etc.
# Lists are dynamic sized.
arr.append(4) # add to end
arr.append(5)
print(arr) # [1, 2, 3, 4, 5]

arr.pop() # remove from end
print(arr) # [1, 2, 3, 4]

# unlike push/append and pop, insert takes O(n) time
arr.insert(1, 10) # insert 10 at index 1
print(arr) # [1, 10, 2, 3, 4]

# Initialize arr of size n with all values as some value
n = 5
arr = [0] * n  # [0, 0, 0, 0, 0]
print(arr)

# Careful: -1 is not out of bounds, it means last element
# Negative indexing accesses elements from the end
arr = [1,2,3,4]
print(arr[-1])  # 4
print(arr[-2])  # 3

# Sublists (aka slicing)
# Similar to for loops, the end index is exclusive
arr = [1,2,3,4,5]
print(arr[1:3]) # [2, 3], from index 1 to 2. 3 is exclusive same as for loops
print(arr[:3])  # [1, 2, 3], from start to before index 3
print(arr[2:])  # [3, 4, 5], from index 2 to end
print(arr[:])   # [1, 2, 3, 4, 5], whole array 




# Unpacking arrays.
arr = [1, 2, 3]
a, b, c = arr
print(a, b, c)  # 1 2 

# Be careful: number of variables must match number of elements
# a, b = arr  # ValueError: too many values to unpack (expected 2)
a, b = [1, 2] # this is ok




# Loop through array
nums = [1, 2, 3, 4, 5]

# Using index and length
for i in range(len(nums)):
    print(nums[i])  # Access by index

# Directly iterating over elements. without using index
for num in nums:
    print(num)  # Direct access to elements

# Using enumerate to get index and value
for index, value in enumerate(nums):
    print(index, value)  # Access index and value

# Loop through multiple arrays simultaneously using zip
# with unpacking
arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']
for num, char in zip(arr1, arr2):
    print(num, char)  # Access elements from both arrays

# In Different Length Arrays, zip stops at the shortest
arr1 = [1, 2, 3, 4] # longer array
arr2 = ['a', 'b'] # shorter array
for num, char in zip(arr1, arr2):
    print(num, char)  # Access elements from both arrays