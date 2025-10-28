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
print(int(-3 / 2)) # -1



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

