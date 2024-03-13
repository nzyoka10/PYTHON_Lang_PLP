# String data type
# literal assignment

# first = "Kenya"
# last = "Kwanza"

# print(type(pizza))
# print(type(first) == str)
# print(isinstance(first, bool))
# print(isinstance(first, str))

# # print(type(last) == int)
# # print(isinstance(last, str))

# constructor function
# pizza = str("Pepperoni")
# print(pizza)
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# String Concatenation
# concatenating strings using the + operator or the join() method.
# full_name =  first + " " + last
# print(full_name, "\n")

# Casting a number to string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s. \n"
# print(statement)

# Using f-string formatting (Python version 3.6 and above)
# formatted_statement = f"I like rock music from the {decade}s."
# print(formatted_statement)

# Multiple lines string
# multiline = ''' 
# Hey, how are you?

# I was just checking in.

#                 All good!
# '''

# print(multiline)

# print(3-5+56)

# STRING Methods
first = "Kenya"
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline.strip()))

# Build a menu
# title = "menu".upper()
# print( "\n", title.center(20, "="))
# print("Coffee".ljust(16, ".") + "Kes. 50".rjust(4))
# print("Cup cake".ljust(16, ".") + "Kes. 70".rjust(4))
# print("Tea ".ljust(16, ".") + "Kes. 60".rjust(4))

# print("")

# string index values
# print(first[0]) # first value of a string
# print(first[-1]) # prints last value position
# print(first[:3]) # range of 0 : 3 characters position
# print(first[3:]) # from the third to last 

# Some methods return boolean data
# print(first.startswith("K"))
# print(first.endswith("F"))

# print("")

# Boolean data type
# my_value = True
# x = bool(False)
# print(type(my_value))
# print(isinstance(x, bool))

# Numeric data type

# print('')

# integer type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# print("")

# float type
# gpa = 3.28
# y = float(3.142)
# print(type(gpa))
# print(isinstance(y, float))

# print("")

# complex type
# value = 34+78j
# print(type(value))
# print(value.real)
# print(value.imag)

# print("")

# Built-in functions for numbers
# gpa = 3.28
# print(abs(gpa))
# print(abs(gpa * -1))

# print(round(gpa))
# print(round(gpa, 1))
print("")
# Using import math
import math

gpa = 3.28

print(math.pi)
print(math.sqrt(81))

print(math.sin(gpa))
print(math.sqrt(gpa))

print(math.ceil(gpa))
print(math.floor(gpa))

# pi = math.pi
# print(math.sqrt(19))

# Casting a string to a number
zipcode = "100001"
zip_value = int(zipcode)

print("\n", type(zip_value))
print(zip_value)

# Error if you attempt to cast incorrect data
# zip_value = int("Makindu")












