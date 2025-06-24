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
>>> print("Hello, World!")
Hello, World!

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
   a = 4
   A = "Sally"
   #A will not overwrite a

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

   ## INTRODUCTION
Python is an interpreted, object-oriented language created by Guido van Rossum. It supports multiple programming paradigms and is known for its clear syntax. Python powers applications in AI, data analysis, automation, and web development. Its large community and huge collection of libraries make it highly practical for solving real-world problems.

## Syntax
Python syntax can be executed by writing directly in the Command Line:
>>> print("Hello, World!")
Hello, World!

## Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.
Python will give you an error if you skip the indentation.

##   Comments
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.



### 🧪 Example Code:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Paridhi")
```
