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
