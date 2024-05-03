## Pyhhon OOP Recap

 - [x] **Object :-** Objects are instances of classes. They have attributes and methods associated with them.
- Attributes: These are the variables that belong to an object. They store data about objects.
- Methods: These are functions that belong to an object. They perform actions on objects.
```python
def hello():
    print("Hello, World!")
    
x = 1
y = "Python"
# print(type(x))  # <class 'int'>
# print(type(y))  # <class 'str'>

print_hello = hello
print_hello()  # Hello, World!
```
 - [x] **Classes :-** A class is a blueprint for creating objects (a specific data structure), providing initial values for its attributes and methods and Objects.
  - `Example of a **Python Class**`

```python
class ClassName:
    # Class constructor 
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color    
    # class method, method_1 and method_2
    def method_1(self):
        print("This car is Method 1")
        
    def method_2(self):
        print("This is Method 2")
```
 - [x] **Methods**: method is defined inside a class and it belongs to the class not the instance.