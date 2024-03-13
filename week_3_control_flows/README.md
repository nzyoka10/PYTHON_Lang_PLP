## Week 3 - Control Flows and Functions

###### Python Control Flows and Functions

- Control flows and functions are essential concepts in Python programming that allow you to control the flow of execution and encapsulate reusable pieces of code. 
- This **`README`** provides an overview of control flows and functions in Python, including their syntax, usage, and best practices.

## Control Flow Structures

Python provides several control flow structures to execute code conditionally or iteratively:

- **if-elif-else**: Allows you to execute different blocks of code based on different conditions.
- **for loop**: Iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.
- **while loop**: Executes a block of code repeatedly as long as a specified condition is true.
- **break and continue**: Allows you to control the flow of loops by breaking out of the loop or skipping the current iteration.

```python
# Example of if-elif-else and for loop
def classify_number(num):
    """Classify a number as positive, negative, or zero."""
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

numbers = [1, -2, 0, 5, -10]
for num in numbers:
    classify_number(num)

# Example of while loop with break and continue
num = 10
while num > 0:
    if num == 5:
        num -= 1
        continue
    print(num)
    if num == 3:
        break
    num -= 1
```

### Functions

Functions allow you to encapsulate reusable pieces of code, making your programs more organized, modular, and easier to understand.

###### Defining Functions
- In python a function is defined using the **`def`** keyword followed by the ``function name`` and **parameters** `enclosed in parentheses`. 
- The function body is then indented;-

```python

# Example 1
# below function greets the user.
def greet(name):
    print(f"Hello, {name}!")

#  calling the function
greet(Eric)

# ~ Example 2:
# This function adds two numbers.
def add(a, b):
    return a + b

result = add(3, 5)  # result will be 8
print(result)

```