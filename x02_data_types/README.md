
## Week 2 -  Python Data Types 

Python is a dynamically typed language, meaning you don't need to specify variable types explicitly. Python provides a wide range of built-in data types to handle different kinds of data. Understanding these data types is essential for effective programming. This README provides an overview of the main data types in Python.

### 1. Numeric Types

Python supports several numeric data types:

- **int**: Integer numbers, e.g., 5, -10, 1000.
- **float**: Floating-point numbers, e.g., 3.14, -0.001, 2.0.
- **complex**: Complex numbers, with a real and imaginary part, e.g., 2+3j, -1-0.5j.

### 2. Sequence Types

Sequence data types represent collections of items. The main sequence types in Python are:

- **list**: Ordered collection of items, mutable (modifiable).
- **tuple**: Ordered collection of items, immutable (cannot be changed).
- **range**: Represents a range of numbers.
- **str**: String, a sequence of characters.

### 3. Mapping Type

- **dict**: A collection of key-value pairs, where each key maps to a value.

### 4. Set Types

- **set**: Unordered collection of unique items.
- **frozenset**: Immutable set, similar to set but cannot be changed after creation.

### 5. Boolean Type

- **bool**: Represents Boolean values True and False.

### 6. None Type

- **None**: Represents the absence of a value or a null value.

### Choosing the correct data type

Data type is crucial for efficient programming and memory usage, thus consider the following factors:

- **Mutability**: do you need a mutable or immutable data type
- **Order**: whether order matters or not.
- **Uniqueness**: if duplicates are allowed or not.
- **Performance**: some data types may offer better performance for specific operations.
- **Memory Usage**: consider the memory requirements of different data types.


## Examples

```python
# Numeric types
x = 5
y = 3.14
z = 2 + 3j

# Sequence types
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_str = "Hello, world!"

# Mapping type
my_dict = {"name": "John", "age": 30}

# Set types
my_set = {1, 2, 3}
my_frozenset = frozenset({4, 5, 6})

# Boolean type
is_valid = True

# None type
result = None
```
