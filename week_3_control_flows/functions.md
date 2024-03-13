## Python Functions

- Functions are a fundamental building block of Python programming. 
- They allow you to encapsulate reusable pieces of code, making your programs more organized, modular, and easier to understand. 
- This **`README`** provides an overview of Python functions, including their syntax, usage, and best practices.

## Defining Functions

In Python, you define a function using the `def` keyword followed by the function name and parameters enclosed in parentheses. The function body is then indented.

```python
def greet(name):
    """This function greets the user."""
    print(f"Hello, {name}!")
```
calling a function
```python

# will call the greet function with "Eric" as an argument and, 
# display: Hello, Eric
greet("Eric")  
```

## Documentation of functions
- functions can be documented using docstrings to provide information about their purpose, parameters, and return values.
  
```python
def factorial(n):
    """
        # Calculate the factorial of a number n.
        
        # Args:
        #     n (int): The number whose factorial is to be calculated.
        
        # Returns:
        #     int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```