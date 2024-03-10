## Python Operators

Operators in Python are symbols that perform operations on variables and values. Python provides a variety of operators to carry out tasks such as arithmetic operations, comparison, logical operations, assignment, membership testing, identity testing, and bitwise operations. Understanding these operators is essential for effective programming in Python.

This README file aims to provide an overview of the different types of operators available in Python and their usage.

### Table of Contents

1. [Arithmetic Operators](#arithmetic-operators)
2. [Comparison Operators](#comparison-operators)
3. [Logical Operators](#logical-operators)
4. [Assignment Operators](#assignment-operators)
5. [Membership Operators](#membership-operators)
6. [Identity Operators](#identity-operators)
7. [Bitwise Operators](#bitwise-operators)

#### Arithmetic Operators <a name="arithmetic-operators"></a>

The arithmetic operators perform operations on numeric data types such as `int`, `float`. 
Also, are used to perform mathematical operations like addition, subtraction, multiplication, division, etc.

- `+` Addition: *returns* `the SUM` of two operands
- `-` Subtraction : *returns* `the DIFFERENCE` of two operands
- `*` Multiplication : *returns*  `the PRODUCT` of two operands
- `/` Division : *returns* `the DIVISION` of two operands
- `%` Modulus (remainder of the division) : *returns* `the REMAINDER` of two operands
- `//` Floor Division - *division that results into whole number* adjusted to the left in the number line
- `**` Exponentiation - ``raises the left operand`` **to the** `power of the right operand`

```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a // b) # Output: 3
print(a ** b) # Output: 1000
```