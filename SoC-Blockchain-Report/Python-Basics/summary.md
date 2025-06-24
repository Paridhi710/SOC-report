# 🐍 Python Basics

Covered:
- Variables and Data Types
- Input/Output
- Conditional Statements (if/else)
- Loops (for, while)
- Functions and Exception Handling

 ## INTRODUCTION
Python is an interpreted, object-oriented language created by Guido van Rossum. It supports multiple programming paradigms and is known for its clear syntax. Python powers applications in AI, data analysis, automation, and web development. Its large community and huge collection of libraries make it highly practical for solving real-world problems.

## Syntax
Python syntax can be executed by writing directly in the Command Line:
```python 
>>> print("Hello, World!")
>>> Hello, World!
```
## Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.
Python will give you an error if you skip the indentation.

##   Comments
Comments can be used to explain Python code.
They can be used to make the code more readable.
They can be used to prevent execution when testing code.
Comments starts with a #.

## Variables
Variables are containers for storing data values.
Python has no specific command for declaring a variable , it is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type, and can even change type after they have been set.

- You can get the data type of a variable with the type() function.
- String variables can be declared either by using single or double quotes
- Variable names are case-sensitive.
  ```python
   >>> a = 4
   >>> A = "Sally"
   >>> #A will not overwrite a
  ```

### Variable name
 A variable can have a short name (like x and y) or a more descriptive name (age, yourname, total_area).

Rules for Python variables:

- A variable name must start with a letter or the underscore character.
- It cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9,   and _ )
- Variable names are case-sensitive. (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

### Global variable
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

## Datatype
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	dict
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview

## Python Strings
Strings in Python are sequences of characters enclosed in single or double quotes. They are immutable, meaning once created, their contents cannot be changed. You can access specific characters using indexing (like text[0]) and get substrings using slicing (like text[0:5]).
Common operations on strings include concatenation using +, repetition using *, and membership checks using the in keyword.
Python strings support a wide range of built-in methods for manipulation and transformation.

## Escape Characters
Escape characters allow you to insert special characters inside strings that would otherwise be difficult to type. An escape character is represented by a backslash (\) followed by a character.
Common escape sequences include \n for newline, \t for tab, \" for double quote, and \\ for a literal backslash.
For example, the string "Hello\nWorld" will print Hello on one line and World on the next. Escape characters are especially useful for formatting output and handling special characters in strings.

## String Methods
Python provides many built-in string methods that make it easy to work with text data.
Some common methods include:
- .upper() and .lower() to change case
- .strip() to remove extra space
- .replace("a", "b") to replace characters or words
- .split() to break a string into a list
- .find("text") to get the index of a substring
These methods make it easy to clean, search, and modify text in Python programs.

## Python Booleans
Booleans are data types that represent one of two values: True or False.
They are commonly used in decision-making using conditions and loops. For example, 5 > 3 evaluates to True.
You can also convert other data types to booleans using the bool() function. An empty string, 0, or None evaluates to False, while non-empty strings and non-zero numbers evaluate to True.
Booleans are used with logical operators like and, or, and not to build complex conditions.

## Python Operators
Python provides several types of operators to perform operations on variables and values:
- Arithmetic Operators: +, -, *, /, %, **, //
- Comparison Operators: ==, !=, >, <, >=, <=
- Logical Operators: and, or, not
- Assignment Operators: =, +=, -=, etc.
- Bitwise, Identity, and Membership Operators also exist.
Operators are used in expressions to carry out computations and make logical decisions in code.

## Python Lists
Lists are ordered, mutable collections used to store multiple items in a single variable.
They are defined using square brackets, like my_list = [1, 2, 3].
Lists can hold elements of different types (numbers, strings, even other lists).
Common list operations include append(), insert(), pop(), remove(), and sort().
You can access elements using indices, slice lists, and iterate through them using loops.

## Python Tuples
Tuples are ordered, immutable collections, meaning once created, their contents cannot be changed.
They are written using parentheses, like my_tuple = (1, 2, 3).
Tuples support indexing, slicing, and can contain elements of different types.
Because of their immutability, tuples are faster and often used to store fixed data like coordinates or settings.
Basic operations like count() and index() are available for tuple objects.

## Python Sets
Sets are unordered collections of unique items. They are written using curly braces, like my_set = {1, 2, 3}.
Duplicates are automatically removed in sets, and the order of elements is not guaranteed.
Useful set methods include add(), remove(), union(), intersection(), and difference().
Sets are ideal for membership tests and removing duplicates from data.
Because they are unordered, elements cannot be accessed using indexes.

## Python Dictionaries
Dictionaries are unordered collections of key-value pairs.
They are defined using curly braces with a colon separating keys and values, like student = {"name": "Paridhi", "age": 20}.
Dictionaries are mutable and allow fast access to values using their keys.
You can add, update, or delete key-value pairs using dict[key] = value, del, or update() methods.
They are widely used in Python for storing structured data like JSON responses or config settings.

## Python If...Else
Conditional statements allow you to execute code only if a certain condition is true.
Python uses if, elif, and else blocks to control the flow:
- if checks a condition
- elif adds more conditions
- else runs if none of the above conditions are true
Proper indentation is important to define which code belongs to which condition. This is essential for decision-making in programs.

## Python Match
The match statement (introduced in Python 3.10) is similar to switch-case in other languages.
It allows you to match a variable against multiple patterns:
```python
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
```
It’s a clean way to handle multiple fixed condition checks, making the code more readable and structured.

## Python While Loops
while loops execute a block of code repeatedly as long as the given condition is True.
They are useful when the number of iterations is not known in advance.
Always ensure that the condition will eventually become false to avoid infinite loops.
You can use break to exit the loop early and continue to skip an iteration.

## Python For Loops
for loops are used to iterate over sequences such as lists, strings, or ranges.
They automatically go through each item in the sequence:
```python
for item in my_list:
    print(item)
```
You can combine it with range() for numeric loops. break and continue also work inside for loops to control flow.

## Python Functions
Functions are reusable blocks of code that perform a specific task.
They are defined using the def keyword followed by a function name and parentheses.
You can pass data to functions through parameters and return results using return.
Functions help in breaking down a large program into smaller, manageable pieces, improving code readability and reusability.
Python also supports default, keyword, and variable-length arguments for flexibility.



### 🧪 Example Code:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Paridhi")
```
