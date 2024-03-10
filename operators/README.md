## Python Operators

- Operators in Python are symbols that perform operations on variables and values.
- Python provides a variety of operators to carry out tasks such as `arithmetic operations`, comparison, `logical operations`, assignment, `membership testing`, ``identity testing``, and `bitwise operations`. 
- Understanding these operators is essential for effective programming in Python.

This README file provides an overview of the different types of operators available in Python and their usage.

### Table of Contents
- [Python Operators](#python-operators)
  - [Table of Contents](#table-of-contents)
    - [Arithmetic Operators ](#arithmetic-operators-)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
      - [Figure 1](#figure-1)
    - [Assignment Operators](#assignment-operators)
    - [Membership Operators](#membership-operators)
        - [Figure 2](#figure-2)
    - [Identity Operators](#identity-operators)
        - [Figure 3](#figure-3)
    - [Bitwise Operators](#bitwise-operators)
        - [Figure 4](#figure-4)

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

#### Comparison Operators
- Used to compare two values. 
- They return True or False based on the comparison result.

|Operator | Meaning                   | Example     | Result |
|---------|----------------------------|--------------|--------|
| ==      | Equal To                                     | `3==2+1`  | False  |
| !=      | Not equal To                | `3!=2+1`   | True   |
| >       | Greater Than                             | `4>3`        | True   |
| <       | Less Than                                                            | `6<9`         | True   |
| >=      | Greater than or Equal To               | `5>=2`                   | True   |
| <=      | Less Than or Equal To              | `8<=8`                                          | True   |
| <>      | NotEqualTo(NotEqual operator)           | `3<>2+1`                                     | True   |
| ==/!=/= | Equality / Inequality            | `3==2+1` , `3!=2+1` | False,True |   

#### Logical Operators
- The Logical operators are used to combine conditional statements, 
- they work with Boolean (`True`/`False`) values and returns a single Boolean value.

##### Figure 1
|Operator | Meaning                   | Example     | Result |
|---------|----------------------------|--------------|--------|
| AND     | Return True if both are True | `x>5 and y<7`  | True  |
| OR      | Return True if either is True | `x>5 or y<7`   | True  |
| NOT     | Return True if expression is False | `not x>5`   | True  |

**`Note:`** python provides three logical operators: `and`, `or`, and `not`.

<!-- Assignment Operators
Assignment operators are used to assign values to variables -->
#### Assignment Operators
- Assignment operators are used to assign values to variables.

|Operator | Meaning                   | Example     |
|---------|----------------------------|--------------|
| =       | Simple assignment          | `x=3`       | None   |
| +=      | Addition and assignment       | `x+=3`      | None   |
| -=      | Subtraction and assignment  | `x-=3`      | None   |
| *=      | Multiplication and assignment | `x*=3`      | None   |
| /=      | Division and assignment     | `x /=3` | None |
| //=     | Integer division and assignment | `x//=3` | None |
| %=      | Modulus and assignment | `x%=3` | None |
| **=     | Exponentiation and assignment | `x**=3` | None |

#### Membership Operators
- Membership operators are used to test if a sequence is presented in an object.
- 
###### Figure 2
|Operator | Meaning                   | Example     | Result |
|---------|----------------------------|--------------|--------|
| In      | Returns True if element exists in the sequence (list, tuple, set). | `'a'in 'abc'` | True   | |
| Not In  | Returns True if element does not exist in the sequence.             |`'b'not in 'abc'` | True   | |

#### Identity Operators
- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

###### Figure 3
|Operator | Meaning                   | Example     | Result |
|---------|----------------------------|--------------|--------|
| `==`      | Returns **`True`** if both operands refer to the **`same object`**. | `x == y`    | True   |
| `is`      | Returns **`True`** if both operands **`refer to the exact same object`**. | `x is y` | True   |
| `is not` | Returns **`True`** if both operands do not refer to the exact same object. | `x is not y` | True   |


#### Bitwise Operators
- Bitwise operators perform bit-level manipulation operations.

###### Figure 4

|Operator | Meaning                   | Example     | Result |
|---------|----------------------------|--------------|--------|
| `&, and`      | Performs a bitwise AND operation on each pair of bits from two operands. | `7 & 5`     | 5        |
| **`or, \|`** | Performs a bitwise OR operation on each pair of bits from two operands. | `(5 &#187; 3) == 5 \| 3` | True   |
| **`^, XOR`** | Performs a bitwise XOR operation on each pair of bits from two operands. | `(10) ^ (4)` | True |
| **`~, not`** | bitwise NOT | Bitwise OR operation on each pair of bits from two operands. | `~(5)` | -6 |
|**`<<, shift left`** | Shift left; zeroes are shifted into the vacant positions from the right. | `7 << 2` | 56 |
| **`>>, shift right`** | Shift right;  zeroes are filled into the vacant places from the left. | `9 >> 2` | 2 |

```python
a = 60  # 0011 1100
b = 13  # 0000 1101

print(a & b)  # Output: 12 (0000 1100)
print(a | b)  # Output: 61 (0011 1101)
print(a ^ b)  # Output: 49 (0011 0001)
print(~a)     # Output: -61 (1100 0011)
print(a << 2) # Output: 240 (1111 0000)
print(a >> 2) # Output: 15 (0000 1111)

```





