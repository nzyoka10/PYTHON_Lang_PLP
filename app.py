# write a program that accepts  user input to create a list of integers.
# Then, compute the sum of all the integers in the list


''' 
    # numeric data type
        -> integer - wholes / both (+Ve and -Ve) numbers ( from 0 to 9 (Natural numbers)
        -> float - decimal numbers 
        -> complex - scientific notations
'''
#  integer data type
# age = 34
# temp = -24
# print(age)
# print(type(age)) # print data type <class 'int'>

# # print out the temp
# print(isinstance(temp, int)) # print data type <class 'int'>
# print(temp)

# simple calc
# num_1 = int(3)
# num_2 = int(3)
# print(num_1)

# print("{------- my calculator program--------------} \n")
# # print("{---== enter numbers  == -----}")
# num_1 = int(input('Enter the number:->:: '))
# num_2 = int(input('Enter second number:->:: '))

# # sum of num_1 and num_2
# sum = (num_1 + num_2)
# print("Sum is :: ", sum)

# # print the product of num_1 and num_2
# product = (num_1 * num_2)
# print("Product is:: ", product)

# # print the difference between num_1 and num_2
# difference = (num_1 - num_2)
# print("Difference is:: ", difference)

# # print division between num_1 and num_2
# divide = (num_1 / num_2)
# print("Divide is:: ", divide)

# # print the modulus between num_1 and num_2
# module = (num_1 % num_2)
# print("Modulus is:: ", module)


# # FLOAT DATA TYPE
# width = 24.74
# height = width + 4 # height == "value give ADD width"

# print("My width is: ", + width)
# print(isinstance(width, float)) # print data type <class 'float'>

# # print height
# print("My height is: ", + height)
# print(isinstance(height, float)) # print data type <class 'float'>

#  Complex data type
# gramma = 56+5j
# print(gramma)
# print(isinstance(gramma, float)) # print data type <class 'float'> (RETURNS False)
# print(isinstance(gramma, complex)) # print data type <class 'complex'> (RETURNS True)

# =================================================================

# String data type
# BOTH ' Single Quotes' and "Double Quotes" used to declare strings in Python.
# OR the first and last names can be concatenated (using the + sign) with each other
# string operations
# first_name = "ERIC"
# last_name = 'NZYOKA'
# full_name = first_name + "-" + last_name

# #  string slicing
# print("Full name is: ", full_name[:]) # prints the full name
# print("Full name at [-1] : ",full_name[-1]) # prints the last charater '<A>' in variable full_name
# print("Full name at [0-9] : ", full_name[0-9]) # print '<I>' in variable full_name
# print("Full name at [0:9] : ", full_name[0:9]) # print '<IC-N>' in variable full_name
# print("Full name at [2:6] : ", full_name[2:6]) # print '<ERIC-NZYO' in variable full_name


# first_name = input("First name: ", str(first_name))
# print(first_name)

#  print full_name
# print(first_name)
# print(last_name)
# print(first_name + ' ' + last_name)
# print(full_name)
# print("Full Name is: ", full_name)

# Sequence data type :: List, Tuple, or Range

# A Python list contains items separated by commas and enclosed within square brackets (` [ ] `). 
print('\n')
#  example
# my_list = [2024, "Python", 3.11, 4+5j, 1.23E-4, "Kenya"]
# print("List is: ", my_list)
# print(type(my_list), '\n')

#  List of  cars
# my_cars = ["Mark X", "Nissan GTR", "Toyota GT4", "Syperd", "Bugatti"]
# print(isinstance(my_cars, list))
# print("List of cars: ", my_cars)

#  Example 3
# nested_listed = [
#     [7, 'One', 'Two', 'Three', 'Four', 'Five'],
    
#     [5, 4, 3, 2, 1, "Python Lang"],
    
#     ['Hello', 2.8, 1.2, 6.3, 1.4, 4.5]
# ]

# print(isinstance(nested_listed, list))
# print("Nested list: ", nested_listed, '\n')
# print("Nested list: ", nested_listed[-1], '\n')
# print("Nested list: ", nested_listed[-2], '\n')
# print("Nested list: ", nested_listed[-3], '\n \n')

# print("Nested list: ", nested_listed[0], '\n')
# print("Nested list: ", nested_listed[1], '\n')
# print("Nested list: ", nested_listed[2], '\n \n')

#  list example 4
# list = ['abcd', 345, 3.47, 'Kenya', 20.4]
# tiny_list = [123, 'Kenya']

#  print complete list
# print("List: ", list)

# print first element of the list
# print("First element of List: ", list[0])

#  print last element of the list
# print("Last element of List: ", list[-1])

# print elements starting from 2nd till 3rd element
# print("Elements starting from 2nd till 3rd element: ", list[1:3])

# print elements starting from 3rd element 
# print("Elements starting from 3rd element: ", list[2:])

# print elements starting from 4th element
# print("Elements starting from 4th element: ", list[3])

# print list two times
# print("List two times: ", list * 2, '\n')

#  print tiny_list
# print("Tiny list : ", tiny_list)
# print("Tiny list two times : ", tiny_list *2)

# concatenated list and tiny_list
# print("Concatenated list : ", list + tiny_list)

# Python Tuple data type
#  Is a sequence data type similar to List.
# a tuple consists of a number of values separated by commas. 
# Unlike lists, however, tuples are enclosed within parentheses (...).

#  example 1 (tuple)
my_tuple = (2024, "hello world", 3+4j, 1.23e-4)

print(type(my_tuple))
print(isinstance(my_tuple, tuple))

print(my_tuple[2])
print(type(my_tuple[2]))

print(my_tuple[3])
print(type(my_tuple[3]))














