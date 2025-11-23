# Junior Software Engineer (Python) - Exam Master Notes
## Singularity Limited - Initial Screening Test Preparation

**Exam Format:** 100 MCQ Questions | 30 Minutes | 165 Total Marks  
**Speed Required:** ~18 seconds per question  
**Focus Areas:** Core Python, OOP, DSA, Django/Flask/FastAPI, DBMS, REST APIs

---

## Table of Contents
1. [Exam Strategy](#exam-strategy)
2. [Core Python Fundamentals](#core-python-fundamentals)
3. [Data Structures & Algorithms](#data-structures--algorithms)
4. [Object-Oriented Programming](#object-oriented-programming)
5. [Web Frameworks (Django/Flask/FastAPI)](#web-frameworks)
6. [Database & SQL](#database--sql)
7. [REST APIs](#rest-apis)
8. [Git & Version Control](#git--version-control)
9. [Linux Basics](#linux-basics)
10. [Quick MCQ Practice](#quick-mcq-practice)

---

## Exam Strategy

### Time Management
- **18 seconds per question** - Must answer quickly!
- **Skip and return** - Mark difficult questions, come back later
- **No negative marking** - Guess if unsure (usually)
- **Read carefully** - Watch for "NOT", "EXCEPT", "INCORRECT"

### Common MCQ Patterns
1. **Output prediction** - What does this code print?
2. **Error identification** - Which line has an error?
3. **Concept questions** - What is the purpose of...?
4. **Best practice** - Which is the correct way to...?
5. **Fill in the blank** - Complete the code

### Priority Order (if short on time)
1. ⭐⭐⭐ Core Python basics (variables, data types, operators)
2. ⭐⭐⭐ Common functions and methods
3. ⭐⭐ OOP concepts (classes, inheritance)
4. ⭐⭐ Basic DSA (lists, loops, conditionals)
5. ⭐ Framework-specific questions

---

## Core Python Fundamentals

### Data Types & Variables

**Quick Facts:**
```python
# Immutable: int, float, str, tuple, frozenset
# Mutable: list, dict, set

# Type checking
type(42)          # <class 'int'>
isinstance(42, int)  # True

# Type conversion
int("10")         # 10
str(42)           # "42"
float(10)         # 10.0
bool(0)           # False
bool(1)           # True
```

**MCQ Pattern:**
```python
Q: What is the output?
x = 5
y = x
y = 10
print(x)

A) 5  ✓  (integers are immutable)
B) 10
C) Error
D) None
```

### Operators

**Quick Reference:**
```python
# Arithmetic: +, -, *, /, //, %, **
10 // 3    # 3 (floor division)
10 % 3     # 1 (modulo)
2 ** 3     # 8 (power)

# Comparison: ==, !=, <, >, <=, >=
# Logical: and, or, not
# Identity: is, is not
# Membership: in, not in

# Common Traps:
5 == 5.0        # True (value comparison)
5 is 5.0        # False (different types)
[1,2] == [1,2]  # True (value)
[1,2] is [1,2]  # False (different objects)
```

### Strings

**Must Know Methods:**
```python
s = "Hello World"

# Case
s.lower()           # "hello world"
s.upper()           # "HELLO WORLD"
s.title()           # "Hello World"
s.capitalize()      # "Hello world"
s.swapcase()        # "hELLO wORLD"

# Search
s.find("World")     # 6 (index, -1 if not found)
s.index("World")    # 6 (raises ValueError if not found)
s.count("l")        # 3
s.startswith("He")  # True
s.endswith("ld")    # True

# Modify
s.replace("World", "Python")  # "Hello Python"
s.split()           # ["Hello", "World"]
" ".join(["a","b"]) # "a b"
s.strip()           # Remove whitespace
s.lstrip()          # Left strip
s.rstrip()          # Right strip

# Check
s.isalpha()         # False (space)
s.isdigit()         # False
s.isalnum()         # False
s.islower()         # False
s.isupper()         # False

# Formatting
"Hello {}".format("World")
f"Hello {name}"     # f-string (Python 3.6+)
```

**Common MCQs:**
```python
Q: "python".capitalize() returns?
A) "Python"  ✓

Q: "hello".find("x") returns?
A) -1  ✓ (not found)

Q: len("python") returns?
A) 6  ✓
```

### Lists

**Essential Operations:**
```python
lst = [1, 2, 3, 4, 5]

# Access
lst[0]              # 1
lst[-1]             # 5
lst[1:3]            # [2, 3] (slicing)
lst[::-1]           # [5,4,3,2,1] (reverse)

# Modify
lst.append(6)       # Add to end
lst.insert(0, 0)    # Insert at index
lst.extend([7,8])   # Add multiple
lst.remove(3)       # Remove first occurrence
lst.pop()           # Remove and return last
lst.pop(0)          # Remove and return at index
lst.clear()         # Empty list

# Search
lst.index(3)        # First index of 3
lst.count(2)        # Count occurrences
3 in lst            # True/False

# Sort
lst.sort()          # In-place
sorted(lst)         # Returns new list
lst.reverse()       # In-place reverse
reversed(lst)       # Returns iterator

# Other
len(lst)            # Length
min(lst)            # Minimum
max(lst)            # Maximum
sum(lst)            # Sum of elements
```

**List Comprehension:**
```python
# Basic
[x*2 for x in range(5)]  # [0,2,4,6,8]

# With condition
[x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

# Nested
[[i*j for j in range(3)] for i in range(3)]
```

### Tuples

**Key Points:**
```python
t = (1, 2, 3)

# Immutable - cannot change
# t[0] = 10  # TypeError

# Access same as lists
t[0]                # 1
t[-1]               # 3

# Methods (only 2!)
t.count(2)          # Count
t.index(2)          # Index

# Single element tuple
single = (1,)       # Note the comma!
not_tuple = (1)     # This is just int

# Tuple unpacking
a, b, c = (1, 2, 3)
```

### Dictionaries

**Must Know:**
```python
d = {"name": "John", "age": 30}

# Access
d["name"]           # "John"
d.get("name")       # "John"
d.get("city", "N/A")  # Default if not found

# Modify
d["age"] = 31       # Update
d["city"] = "NYC"   # Add new
del d["age"]        # Delete
d.pop("name")       # Remove and return
d.clear()           # Empty dict

# Methods
d.keys()            # dict_keys(['name', 'age'])
d.values()          # dict_values(['John', 30])
d.items()           # dict_items([('name','John'), ('age',30)])

# Check
"name" in d         # True
"name" in d.keys()  # True

# Loop
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Dict comprehension
{x: x**2 for x in range(5)}
```

### Sets

**Quick Guide:**
```python
s = {1, 2, 3}

# Add/Remove
s.add(4)            # Add element
s.remove(2)         # Remove (KeyError if not found)
s.discard(2)        # Remove (no error)
s.pop()             # Remove arbitrary element
s.clear()           # Empty set

# Set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1 | s2             # Union: {1,2,3,4,5}
s1 & s2             # Intersection: {3}
s1 - s2             # Difference: {1,2}
s1 ^ s2             # Symmetric diff: {1,2,4,5}

# Methods
s1.union(s2)
s1.intersection(s2)
s1.difference(s2)

# Empty set
empty = set()       # NOT {} (that's dict!)
```

### Control Flow

**If-Elif-Else:**
```python
if condition:
    pass
elif condition2:
    pass
else:
    pass

# Ternary
result = "even" if x % 2 == 0 else "odd"
```

**Loops:**
```python
# For loop
for i in range(5):      # 0 to 4
    print(i)

for i in range(1, 6):   # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# Break, Continue, Pass
for i in range(10):
    if i == 5:
        break       # Exit loop
    if i % 2 == 0:
        continue    # Skip to next iteration
    pass            # Do nothing (placeholder)

# Else with loops
for i in range(5):
    print(i)
else:
    print("Done")   # Executes if loop completes normally
```

### Functions

**Basics:**
```python
# Define
def greet(name):
    return f"Hello {name}"

# Default arguments
def greet(name="World"):
    return f"Hello {name}"

# Multiple return values
def get_stats():
    return 10, 20, 30
a, b, c = get_stats()

# *args (tuple)
def sum_all(*args):
    return sum(args)
sum_all(1, 2, 3, 4)  # 10

# **kwargs (dict)
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
print_info(name="John", age=30)

# Lambda
square = lambda x: x**2
square(5)  # 25

# Map, Filter, Reduce
list(map(lambda x: x*2, [1,2,3]))  # [2,4,6]
list(filter(lambda x: x>2, [1,2,3,4]))  # [3,4]

from functools import reduce
reduce(lambda x,y: x+y, [1,2,3,4])  # 10
```

### Common Built-in Functions

**Must Remember:**
```python
# Type conversion
int(), float(), str(), list(), tuple(), set(), dict()

# Math
abs(-5)             # 5
round(3.7)          # 4
pow(2, 3)           # 8
divmod(10, 3)       # (3, 1)

# Sequence
len([1,2,3])        # 3
min([1,2,3])        # 1
max([1,2,3])        # 3
sum([1,2,3])        # 6
sorted([3,1,2])     # [1,2,3]
reversed([1,2,3])   # iterator

# Iteration
range(5)            # 0,1,2,3,4
enumerate(['a','b']) # (0,'a'), (1,'b')
zip([1,2], ['a','b'])  # (1,'a'), (2,'b')

# Type checking
type(42)
isinstance(42, int)

# Object
id(obj)             # Memory address
dir(obj)            # List attributes

# Input/Output
print("Hello")
input("Enter: ")    # Returns string

# Boolean
all([True, True])   # True (all elements True)
any([True, False])  # True (at least one True)
bool(0)             # False
```

---

## Data Structures & Algorithms

### Time Complexity (Big O)

**Must Know:**
```
O(1)      - Constant     - dict/set lookup, list index
O(log n)  - Logarithmic  - Binary search
O(n)      - Linear       - Single loop, list search
O(n log n)- Log-linear   - Efficient sort (merge/quick)
O(n²)     - Quadratic    - Nested loops, bubble sort
O(2ⁿ)     - Exponential  - Fibonacci (naive)
```

**Common Operations:**
```python
# List
list[i]         # O(1) - access by index
list.append()   # O(1) - add to end
list.insert(0)  # O(n) - insert at beginning
list.pop()      # O(1) - remove from end
list.pop(0)     # O(n) - remove from beginning
x in list       # O(n) - search

# Dict/Set
dict[key]       # O(1) - access
dict[key] = val # O(1) - insert/update
x in dict       # O(1) - search
```

### Searching Algorithms

**Linear Search:**
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Time: O(n)
```

**Binary Search (sorted array):**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Time: O(log n)
```

### Sorting Algorithms

**Bubble Sort:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Time: O(n²), Space: O(1)
```

**Quick Facts:**
```
Bubble Sort:    O(n²)
Selection Sort: O(n²)
Insertion Sort: O(n²)
Merge Sort:     O(n log n)
Quick Sort:     O(n log n) average
```

### Common Problems

**Reverse a List:**
```python
# Method 1
arr[::-1]

# Method 2
arr.reverse()

# Method 3
reversed(arr)
```

**Find Max/Min:**
```python
max(arr)
min(arr)
```

**Count Occurrences:**
```python
arr.count(element)
# or
from collections import Counter
Counter(arr)
```

**Remove Duplicates:**
```python
list(set(arr))  # Loses order
# or
list(dict.fromkeys(arr))  # Preserves order
```

**Palindrome Check:**
```python
s == s[::-1]
```

**Fibonacci:**
```python
# Recursive
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Iterative
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**Factorial:**
```python
# Recursive
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Iterative
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```

**Prime Check:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

---

## Object-Oriented Programming

### Classes and Objects

**Basic Class:**
```python
class Person:
    # Class variable (shared by all instances)
    species = "Human"
    
    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # Class method
    @classmethod
    def create_adult(cls, name):
        return cls(name, 18)
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Create object
p = Person("John", 30)
print(p.name)        # John
print(p.greet())     # Hello, I'm John
```

### Inheritance

**Single Inheritance:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.speak())   # Woof!
```

**Method Overriding:**
```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
        super().show()  # Call parent method
```

**Multiple Inheritance:**
```python
class A:
    def method_a(self):
        pass

class B:
    def method_b(self):
        pass

class C(A, B):  # Inherits from both A and B
    pass
```

### Encapsulation

**Access Modifiers:**
```python
class BankAccount:
    def __init__(self):
        self.public = "Public"          # Public
        self._protected = "Protected"    # Protected (convention)
        self.__private = "Private"       # Private (name mangling)
    
    def get_balance(self):
        return self.__private

acc = BankAccount()
print(acc.public)        # OK
print(acc._protected)    # OK (but shouldn't)
# print(acc.__private)   # Error!
print(acc.get_balance()) # OK
```

### Polymorphism

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Different implementation
```

### Magic Methods (Dunder)

**Common Ones:**
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        # print(book)
        return f"{self.title} ({self.pages} pages)"
    
    def __repr__(self):
        # Developer representation
        return f"Book('{self.title}', {self.pages})"
    
    def __len__(self):
        # len(book)
        return self.pages
    
    def __eq__(self, other):
        # book1 == book2
        return self.pages == other.pages
    
    def __lt__(self, other):
        # book1 < book2
        return self.pages < other.pages
    
    def __add__(self, other):
        # book1 + book2
        return self.pages + other.pages
```

### Key OOP Concepts for MCQs

**Q: What is encapsulation?**  
A: Hiding internal details and providing public interface

**Q: What is inheritance?**  
A: Acquiring properties and methods from parent class

**Q: What is polymorphism?**  
A: Same interface, different implementations

**Q: What is abstraction?**  
A: Hiding complex implementation, showing only essential features

**Q: What does `super()` do?**  
A: Calls method from parent class

**Q: What is `self`?**  
A: Reference to current instance of class

**Q: Difference between class variable and instance variable?**  
A: Class variable is shared, instance variable is unique to object

---

## Web Frameworks

### Django Basics

**Key Concepts:**
```python
# MTV Pattern
Model - Database layer
Template - Presentation layer
View - Business logic layer

# Project structure
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        models.py
        views.py
        urls.py
        templates/
```

**Models (ORM):**
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Common field types:
CharField, IntegerField, EmailField, DateField,
DateTimeField, BooleanField, TextField, 
ForeignKey, ManyToManyField
```

**Views:**
```python
# Function-based view
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def detail(request, id):
    return HttpResponse(f"Student {id}")

# Class-based view
from django.views import View

class StudentView(View):
    def get(self, request):
        return HttpResponse("GET request")
    
    def post(self, request):
        return HttpResponse("POST request")
```

**URLs:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/<int:id>/', views.detail, name='detail'),
]
```

**Common Commands:**
```bash
django-admin startproject myproject
python manage.py startapp myapp
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Flask Basics

**Simple App:**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple route
@app.route('/')
def home():
    return "Hello World"

# Route with parameter
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"

# Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Logging in..."
    return "Login page"

# JSON response
@app.route('/api/data')
def get_data():
    return jsonify({'name': 'John', 'age': 30})

if __name__ == '__main__':
    app.run(debug=True)
```

**Common Patterns:**
```python
# Get request data
request.args.get('name')      # Query parameters (?name=John)
request.form.get('email')     # Form data
request.json.get('data')      # JSON data

# Templates
from flask import render_template
return render_template('index.html', name='John')

# Redirect
from flask import redirect, url_for
return redirect(url_for('home'))
```

### FastAPI Basics

**Simple API:**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Simple route
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Query parameter
@app.get("/search")
def search(q: str = None):
    return {"query": q}

# Request body with Pydantic
class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
```

**Key Features:**
- Automatic validation
- Auto-generated docs (/docs)
- Type hints required
- Async support

### Framework Comparison MCQs

**Q: Which is lighter - Django or Flask?**  
A: Flask (micro-framework)

**Q: Django follows which pattern?**  
A: MTV (Model-Template-View)

**Q: Which framework has built-in ORM?**  
A: Django

**Q: FastAPI is based on?**  
A: Starlette and Pydantic

**Q: Which supports async/await natively?**  
A: FastAPI

---

## Database & SQL

### SQL Basics

**Common Commands:**
```sql
-- SELECT
SELECT * FROM users;
SELECT name, email FROM users;
SELECT * FROM users WHERE age > 18;
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users LIMIT 10;

-- INSERT
INSERT INTO users (name, email, age) 
VALUES ('John', 'john@email.com', 30);

-- UPDATE
UPDATE users SET age = 31 WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;

-- JOINS
SELECT u.name, o.order_id
FROM users u
JOIN orders o ON u.id = o.user_id;

-- Aggregations
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT MAX(salary) FROM employees;
SELECT MIN(price) FROM products;
SELECT SUM(amount) FROM orders;

-- GROUP BY
SELECT country, COUNT(*) 
FROM users 
GROUP BY country;

-- HAVING
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- WHERE vs HAVING
WHERE  - filters rows before grouping
HAVING - filters groups after grouping
```

### Database Concepts

**ACID Properties:**
```
A - Atomicity: All or nothing
C - Consistency: Valid state always
I - Isolation: Transactions don't interfere
D - Durability: Changes are permanent
```

**Keys:**
```
Primary Key: Unique identifier
Foreign Key: Reference to another table
Unique Key: Unique but can be NULL
Composite Key: Multiple columns as key
```

**Normalization:**
```
1NF: No repeating groups, atomic values
2NF: 1NF + No partial dependencies
3NF: 2NF + No transitive dependencies
```

**Index:**
- Speeds up queries
- Slows down INSERT/UPDATE
- Created on frequently searched columns

### Python Database (sqlite3)

**Basic Usage:**
```python
import sqlite3

# Connect
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

# Insert
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
               ('John', 'john@email.com'))

# Query
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Query one
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
row = cursor.fetchone()

# Commit and close
conn.commit()
conn.close()
```

**ORM (SQLAlchemy):**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create engine
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# Create
user = User(name='John', email='john@email.com')
session.add(user)
session.commit()

# Query
users = session.query(User).all()
user = session.query(User).filter_by(id=1).first()
```

---

## REST APIs

### HTTP Methods

```
GET    - Retrieve data (Read)
POST   - Create new resource (Create)
PUT    - Update entire resource (Update)
PATCH  - Partial update (Update)
DELETE - Remove resource (Delete)
```

### HTTP Status Codes

**Must Know:**
```
200 OK - Success
201 Created - Resource created
204 No Content - Success but no data

400 Bad Request - Invalid request
401 Unauthorized - Authentication required
403 Forbidden - No permission
404 Not Found - Resource doesn't exist
405 Method Not Allowed - Wrong HTTP method

500 Internal Server Error - Server error
502 Bad Gateway - Invalid response from upstream
503 Service Unavailable - Server down
```

### REST Principles

**Key Concepts:**
1. **Stateless** - Each request independent
2. **Client-Server** - Separation of concerns
3. **Cacheable** - Responses can be cached
4. **Uniform Interface** - Consistent API design
5. **Resource-based** - URLs represent resources

**Good API Design:**
```
GET    /users          - List all users
GET    /users/1        - Get user by ID
POST   /users          - Create new user
PUT    /users/1        - Update user
DELETE /users/1        - Delete user

# Use nouns, not verbs
✓ GET /users
✗ GET /getUsers

# Use plural
✓ /users
✗ /user

# Versioning
/api/v1/users
```

### JSON

**Python JSON:**
```python
import json

# Python to JSON (serialize)
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# JSON to Python (deserialize)
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)

# File operations
# Write
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read
with open('data.json', 'r') as f:
    data = json.load(f)
```

### API Request (Python)

**Using requests library:**
```python
import requests

# GET request
response = requests.get('https://api.example.com/users')
data = response.json()
print(response.status_code)

# POST request
data = {"name": "John", "age": 30}
response = requests.post('https://api.example.com/users', 
                        json=data)

# With headers
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com/users',
                       headers=headers)

# With parameters
params = {'page': 1, 'limit': 10}
response = requests.get('https://api.example.com/users',
                       params=params)
```

---

## Git & Version Control

### Basic Commands

```bash
# Initialize
git init

# Clone
git clone https://github.com/user/repo.git

# Status
git status

# Add files
git add file.txt
git add .                    # Add all

# Commit
git commit -m "Message"

# Push
git push origin main

# Pull
git pull origin main

# Branch
git branch                   # List branches
git branch feature          # Create branch
git checkout feature        # Switch branch
git checkout -b feature     # Create and switch
git merge feature           # Merge branch
git branch -d feature       # Delete branch

# Stash
git stash                   # Save changes temporarily
git stash pop               # Apply stashed changes

# Log
git log
git log --oneline
```

### Common Workflows

**Feature Branch:**
```bash
1. git checkout -b feature-x
2. (make changes)
3. git add .
4. git commit -m "Add feature x"
5. git push origin feature-x
6. (create pull request)
7. git checkout main
8. git merge feature-x
```

**MCQ Questions:**
```
Q: What does git clone do?
A: Creates a local copy of remote repository

Q: Difference between git pull and git fetch?
A: pull = fetch + merge

Q: What is a branch?
A: Independent line of development

Q: What is a merge conflict?
A: When same lines changed in different branches

Q: What does .gitignore do?
A: Specifies files Git should ignore
```

---

## Linux Basics

### Essential Commands

```bash
# Navigation
pwd                 # Print working directory
ls                  # List files
ls -la              # List all (including hidden)
cd /path            # Change directory
cd ~                # Home directory
cd ..               # Parent directory

# File operations
touch file.txt      # Create file
mkdir dir           # Create directory
rm file.txt         # Remove file
rm -r dir           # Remove directory
cp file1 file2      # Copy
mv file1 file2      # Move/Rename

# View files
cat file.txt        # Display file
less file.txt       # View with pagination
head file.txt       # First 10 lines
tail file.txt       # Last 10 lines
tail -f file.txt    # Follow file (real-time)

# Search
grep "pattern" file.txt
find . -name "*.py"

# Permissions
chmod 755 file.sh   # Change permissions
chown user file.txt # Change owner

# Process
ps                  # List processes
top                 # Real-time processes
kill PID            # Kill process
```

### File Permissions

```
rwxrwxrwx
│││││││││
││││││└──── Others execute
│││││└───── Others write
││││└────── Others read
│││└─────── Group execute
││└──────── Group write
│└───────── Group read
└────────── Owner read/write/execute

Numbers:
7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---

Example:
chmod 755 = rwxr-xr-x
chmod 644 = rw-r--r--
```

---

## Quick MCQ Practice

### Python Basics

**Q1: What is the output?**
```python
print(type([]) == list)
```
A) True ✓  
B) False  
C) Error  
D) None

**Q2: What does `//` operator do?**  
A) Division  
B) Floor division ✓  
C) Exponentiation  
D) Modulo

**Q3: Which is mutable?**  
A) Tuple  
B) String  
C) List ✓  
D) Integer

**Q4: Output of `bool([])`?**  
A) True  
B) False ✓  
C) Error  
D) None

**Q5: `range(5)` generates:**  
A) 1,2,3,4,5  
B) 0,1,2,3,4 ✓  
C) 1,2,3,4  
D) 0,1,2,3,4,5

**Q6: What is `lambda x: x*2` ?**  
A) Function  
B) Anonymous function ✓  
C) Class  
D) Variable

**Q7: `len("python")` returns:**  
A) 5  
B) 6 ✓  
C) 7  
D) Error

**Q8: `[1,2,3] + [4,5]` equals:**  
A) [5,7]  
B) [1,2,3,4,5] ✓  
C) Error  
D) [1,2,3,[4,5]]

**Q9: `dict.get('key', 'default')` returns:**  
A) Error if key not found  
B) None if key not found  
C) 'default' if key not found ✓  
D) Empty string

**Q10: Which is O(1)?**  
A) List search  
B) Dict lookup ✓  
C) List sort  
D) Nested loop

### OOP

**Q11: What is `self`?**  
A) Class name  
B) Instance reference ✓  
C) Method name  
D) Variable

**Q12: `__init__` is:**  
A) Destructor  
B) Constructor ✓  
C) Class method  
D) Static method

**Q13: Which allows multiple inheritance?**  
A) Java  
B) Python ✓  
C) C#  
D) None

**Q14: `super()` is used for:**  
A) Creating new class  
B) Accessing parent class ✓  
C) Deleting object  
D) Type checking

**Q15: Private variable in Python:**  
A) _var  
B) __var ✓  
C) var_  
D) No private variables

### Web/API

**Q16: Django follows which pattern?**  
A) MVC  
B) MTV ✓  
C) MVT  
D) MVVM

**Q17: HTTP status for "Not Found":**  
A) 200  
B) 400  
C) 404 ✓  
D) 500

**Q18: POST method is used to:**  
A) Retrieve data  
B) Create data ✓  
C) Delete data  
D) Update data

**Q19: Flask is a:**  
A) Full-stack framework  
B) Micro-framework ✓  
C) Database  
D) Library

**Q20: JSON stands for:**  
A) JavaScript Object Notation ✓  
B) Java Standard Object Notation  
C) JavaScript Online Notation  
D) None

### Database

**Q21: PRIMARY KEY is:**  
A) Unique identifier ✓  
B) Foreign reference  
C) Index  
D) Constraint

**Q22: JOIN combines:**  
A) Rows  
B) Columns  
C) Tables ✓  
D) Databases

**Q23: SELECT * means:**  
A) Select all columns ✓  
B) Select all rows  
C) Select all tables  
D) Select nothing

**Q24: Which is fastest?**  
A) SELECT with index ✓  
B) SELECT without index  
C) Both same  
D) Depends

**Q25: ACID - A stands for:**  
A) Atomicity ✓  
B) Association  
C) Accuracy  
D) Authentication

### Git/Linux

**Q26: `git clone` does:**  
A) Creates branch  
B) Copies repository ✓  
C) Commits changes  
D) Pushes code

**Q27: `chmod 755` means:**  
A) rwxr-xr-x ✓  
B) rw-r--r--  
C) rwxrwxrwx  
D) r-xr-xr-x

**Q28: `ls -a` shows:**  
A) All files including hidden ✓  
B) Only hidden files  
C) Directory size  
D) File permissions

**Q29: `cd ..` goes to:**  
A) Home directory  
B) Root directory  
C) Parent directory ✓  
D) Previous directory

**Q30: `pip install` is for:**  
A) Installing Python ✓ packages  
B) Creating files  
C) Running scripts  
D) Debugging

---

## Last-Minute Revision Checklist

### ⚡ 5 Minutes Before Exam

**Python:**
- [ ] `list`, `tuple`, `dict`, `set` - mutable vs immutable
- [ ] `range()`, `len()`, `type()`, `isinstance()`
- [ ] String methods: `upper()`, `lower()`, `split()`, `join()`
- [ ] List methods: `append()`, `extend()`, `pop()`, `remove()`
- [ ] `if-elif-else`, `for`, `while`, `break`, `continue`
- [ ] Function syntax, `*args`, `**kwargs`, `lambda`

**OOP:**
- [ ] `class`, `__init__`, `self`
- [ ] Inheritance, `super()`
- [ ] Encapsulation, Polymorphism

**Web:**
- [ ] Django: MTV, models, views, urls
- [ ] Flask: routes, request, jsonify
- [ ] HTTP: GET, POST, PUT, DELETE
- [ ] Status codes: 200, 201, 400, 404, 500

**Database:**
- [ ] SELECT, INSERT, UPDATE, DELETE
- [ ] WHERE, ORDER BY, LIMIT
- [ ] JOIN, GROUP BY, HAVING
- [ ] Primary Key, Foreign Key

**Git:**
- [ ] `clone`, `add`, `commit`, `push`, `pull`
- [ ] `branch`, `checkout`, `merge`

### 🎯 Common Mistakes to Avoid

1. **Read question carefully** - Look for "NOT", "EXCEPT"
2. **Check all options** - Don't rush to first correct-looking answer
3. **Syntax matters** - `print()` not `Print()`
4. **Indentation** - Python is indentation-sensitive
5. **Case sensitive** - `Name` ≠ `name`
6. **Index starts at 0** - `list[0]` is first element
7. **Range exclusive** - `range(5)` is 0 to 4
8. **Return vs Print** - Functions need `return`, not just `print`

### 📝 Common Traps

```python
# Trap 1: Mutable defaults
def append(item, lst=[]):  # WRONG!
    lst.append(item)
    return lst

# Trap 2: is vs ==
[1,2] == [1,2]  # True
[1,2] is [1,2]  # False

# Trap 3: Range
range(5)        # 0,1,2,3,4 (not 1,2,3,4,5)

# Trap 4: Division
5 / 2           # 2.5
5 // 2          # 2

# Trap 5: Global vs Local
x = 10
def func():
    x = 5       # Local x
    print(x)    # Prints 5
func()
print(x)        # Prints 10
```

---

## Exam Day Tips

### Before Starting
1. ✅ Close ALL tabs and applications
2. ✅ Disable browser extensions or use Guest profile
3. ✅ Check webcam and microphone working
4. ✅ Ensure face clearly visible (~0° alignment)
5. ✅ Remove external displays
6. ✅ Quiet environment, alone
7. ✅ Stable internet connection
8. ✅ Use Google Chrome
9. ✅ Full screen mode
10. ✅ Don't use virtual camera

### During Exam
1. **Time**: 30 min / 100 questions = 18 sec/question
2. **Strategy**: Quick scan → Answer easy → Return to difficult
3. **Don't get stuck**: Mark and move on
4. **Guess if needed**: Better than blank (if no negative)
5. **Stay calm**: Face visible, no suspicious movements
6. **No tab switching**: Will be detected
7. **No talking**: Audio monitored
8. **Watch the clock**: Save time for review

### If Technical Issues
- Contact immediately: koly@singularitybd.com
- Don't panic
- Document the issue
- Follow proctor instructions

---

## Practice Questions - Final Round

### Rapid Fire (Answer in 10 seconds each)

1. `print(3 + 2 * 2)` → **7**
2. `print("Hi" * 3)` → **HiHiHi**
3. `print(10 // 3)` → **3**
4. `print(10 % 3)` → **1**
5. `print(bool([]))` → **False**
6. `len("Python")` → **6**
7. `"python".upper()` → **PYTHON**
8. `[1,2,3].append(4)` → **[1,2,3,4]**
9. `list(range(3))` → **[0,1,2]**
10. `type({})` → **dict**
11. Django pattern? → **MTV**
12. Flask type? → **Micro-framework**
13. HTTP GET for? → **Retrieve data**
14. Status 404? → **Not Found**
15. SQL to insert? → **INSERT**
16. Primary key? → **Unique identifier**
17. `git clone` does? → **Copy repository**
18. `chmod 755`? → **rwxr-xr-x**
19. `cd ..` goes? → **Parent directory**
20. `pip` for? → **Install packages**

---

## Summary - Key Takeaways

### Must Remember

**Python:**
- Data types: int, float, str, list, tuple, dict, set
- Mutable: list, dict, set | Immutable: int, str, tuple
- Common methods for each data type
- Control flow: if, for, while, break, continue
- Functions: def, return, *args, **kwargs, lambda

**OOP:**
- class, `__init__`, self
- Inheritance, super()
- Encapsulation, Polymorphism, Abstraction

**Web:**
- Django: MTV, ORM
- Flask: lightweight, routes
- FastAPI: modern, async
- HTTP methods and status codes

**Database:**
- CRUD: SELECT, INSERT, UPDATE, DELETE
- Joins, indexes, keys
- ACID properties

**Tools:**
- Git: clone, add, commit, push, pull, branch
- Linux: ls, cd, pwd, chmod, grep

### Time Allocation (30 minutes)

- **First 15 min**: Answer all easy/confident questions
- **Next 10 min**: Tackle medium difficulty
- **Last 5 min**: Guess remaining, review marked questions

### Confidence Boosters

✓ You know Python basics  
✓ You understand OOP  
✓ You've seen web frameworks  
✓ You know SQL basics  
✓ You're familiar with Git  

**Trust your preparation. Stay calm. Read carefully. You've got this! 🚀**

---

**Good luck with your Singularity Limited exam! 💪**
