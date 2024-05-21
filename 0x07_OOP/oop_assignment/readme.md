# Person Class Assignment
###### Week 04 - OOP
This repository contains a Python class named `Person` that represents a person with attributes such as name, age, and gender. It also includes a method to introduce the person.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/person-class-assignment.git
    ```

2. Navigate to the project directory:

    ```bash
    cd person-class-assignment
    ```

3. Run the Python script to see the example:

    ```bash
    python person.py
    ```

## Code

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Alice", 25, "female")

# Calling the introduce method to display the person's information
person1.introduce()
