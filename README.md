## Python Programming Language

- Python Syntax
```python
    print('Hello World!')
```
- Python indentation 
    - Indentation refers to the spaces at the beginning of a code line.
```python
    if x > 0:
        print('x is positive number')
```
- Python Variables
    - In Python, variables are created when you assign a value to it

```python
    x = 5
    y = "Eric"
```

- Python comments
    - Python has commenting capability for the purpose of in-code documentation.
    - Comments are ignored by Python interpreter, during execution.

```python
    # This is a comment
    print("Python is fun!")
```
- Python variable names
    - A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
        - Rules for Python variables:
            - A variable name must start with a letter or the underscore character
            - A variable name cannot start with a number
            - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
            - Variable names are case-sensitive (age, Age and AGE are three different variables)
            A variable name cannot be any of the Python keywords.

- Global variable
    - Variables that are created outside of a function

    ```python
        x = "awesome"

        def myfunc():
            print("Python is " + x)

        myfunc()
    ```
-  Create a variable inside a function, with the same name as the global variable

```python

    x = "awesome"

    def myfunc():
        x = "fantastic"
        print("Python is " + x)

    myfunc()

    print("Python is " + x)
```
- The global Keyword
    - when you create a variable inside a function, that variable is local, and can only be used inside that function.
    - To create a global variable inside a function, you can use the global keyword.

```python
    def myfunc():
        global x
        x = "fantastic"

    myfunc()
    print("Python is " + x)
```