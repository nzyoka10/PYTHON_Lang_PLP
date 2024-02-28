# data types --> specify the type of data to be stored inside a variable
'''
    # String Data Type: It is used to store text or characters. 
    str_data = "Hello World"
    
    print(type(str_data))   # <class 'str'>

    # Integer Data Type: It is used to store integer values (whole numbers).
    int_data = 10

    print(type(int_data))   # <class 'int'>

    # Float Data Type: It is used to store floating point numbers, which are numbers with a decimal point.
    float_data = 3.14
    
    print(type(float_data)) # <class 'float'>
    
    # Sequence data type: It is used to store sequence numbers, which are numbers with a sequence like in lists, tuples, range.
        # list_languages = ["English", "swahili", "Arab"]
    
    # Boolean data type: It is used to store boolean values, which are boolean values with a boolean value (true/ false).
    
   #Examples below:
    
'''
str_data = "Hello World"
print(type(str_data))   # <class 'str'>
    
int_data = 5
print(type(int_data)) # <class 'int'>

float_data = 3.142
print(type(float_data)) # <class 'float'>

languages = ["Python", "Java", "Swift", "JavaScript"]
print(type(languages)) # <class 'list'>
    # accessing one element of the list
print(languages[0]) # Python

# Accessing multiple elements using slicing
print(languages[0:2]) # ['Python', 'Java']

# Adding new item to the list
languages.append("C++") 
print(languages)

# python tuple data type
# A tuple is an ordered sequence of items same as a list. 
# the ONLY difference is that tuples are immutable while lists are mutable.
# Tuples once created cannot be modified
# in python, the parentheses () is used to store items in a tuple
print('\n')

# example below
product = ('Xbox', 499.99, 'Lisher', 346.72, 'PLP', 'none')
print(product)
print(type(product)) # <class 'tuple'>
print(len(product)) # shows its length
print(product[0]) # Xbox
print(product[1]) # access single element in the tuple
print(product[2]) # access another single element in the tuple

print('\n')

# python String data type
name = 'Python'
print(name)

message = 'Python for beginners'
print(message)

string_var = "This is a string."
print('String Length : ', len(string_var), '\n')

# python Set data type
student_id = {112, 113, 114, 115, 116, 117, 118, 119}
print(student_id)
print(type(student_id))

# example 2
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
print(type(fruits))

# python Dictionary data type
# dictionary --> is an ordered collection of items 
print('\n')
# example of dictionary
capital_city = {
    'USA': 'Washington D.C',
    'Kenya': 'Nairobi',
    'Italy': 'Rome',
    'Tunisia': 'Tunis'
}
print(capital_city)
print(type(capital_city)) #<class 'dict'>
print(capital_city['Kenya']) # Nairobi

# example 2
print('\n')
user_info = {
    'Name': 'Eric Doe',
    'Age': 123,
    'Location': 'Syokimau',
    'County': 'Machakos'
}
print(user_info)
print(len(user_info))



