
### Week 4 - Python OOP 

###### `Object-Oriented Programming`

- `OOP` is a programming paradigm that focuses on organizing code into objects that encapsulate data and behavior.
- Python is an object-oriented programming language that supports the creation and manipulation of objects.

##### Key Concepts in Python OOP

###### `1. Classes and Objects`

- **Class**: A blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have.
- **Object**: An instance of a class. It represents a specific entity with its own unique data and behavior.

###### `2. Inheritance`

- **Inheritance**: A mechanism that allows a class (subclass) to inherit properties and methods from another class (superclass). It promotes code reuse and enables hierarchical relationships between classes.

###### `3. Encapsulation`

- **Encapsulation**: The practice of hiding the internal state of an object and restricting access to it. It promotes data integrity and reduces coupling between components.

###### `4. Polymorphism`

- **Polymorphism**: The ability of different classes to be treated as objects of a common superclass. It allows for flexibility and extensibility in code design.

##### Benefits of Python OOP

- **Modularity**: Code is organized into reusable and maintainable components (classes and objects).
- **Code Reusability**: Objects can be reused across different parts of the program.
- **Flexibility**: OOP supports dynamic modification and extension of code through inheritance and polymorphism.
- **Encapsulation**: Data hiding and abstraction enhance security and reduce complexity.

#### ``Example:``

```python
# Define a simple class
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")

# Create an object of the Dog class
my_dog = Dog("Buddy")

# Call the bark method of the object
my_dog.bark()  # Output: Buddy says woof!
```
