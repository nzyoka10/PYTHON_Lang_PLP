## Pyhhon OOP Recap

#### Classe
-  A class is a blueprint for creating objects (a specific data structure), providing initial values for its attributes and methods and Objects.

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