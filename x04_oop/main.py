
# Python Classes and Objects
# ----------------------------------------------------------------
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

#* How to create a python class
#  the class keyword is used

# class my_class:
#     x = 53

#* create an Object
# p1 = my_class()
# print(p1.x)

# 
#* ------ the __init__() function
#&      The __init__() method is a special method that,
#&       gets called when you create a new instance of a class.
# 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person("Nzyoka",  28)
# person2 = Person("Jane", 34)
# person3 = Person("Mike", 34)

# print(person1.name)
# print(person2.name)
# print(person3.name)

# * ------- Accessing Attributes
#&      You can access attributes using dot notation (.)

# print('Person 1: ', person1.name)

# * -------- Modifying Attributes
#&           To modify an attribute, use the dot notation followed by equals (=).

# person1.name = "Tomh"
# print('Person1 name modified: ', person1.name)



