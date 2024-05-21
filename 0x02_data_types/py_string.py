# Python String
'''
    - Strings in python are surrounded by either single quotation marks, or double quotation marks.
    - 'hello' is the same as "hello".
'''

# Example
# print("Hello World, Line 1")
# print('Hello world, Line 2')

#~ Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the 
# quotes surrounding the string:

# print("It's alright")
# print("He is called 'Eric'")
# print('He is called "Johnny"')

#~ Assign String to a Variable
# a = "Power Learn"
# print(a)

#~ Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

# print(a)

#~ String are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Example
# a = 'Hello, Kenya'
# print(a)
# print(a[1])
# print(a[0:3])

#~ string length
# a = 'Hello, Kenya'
# print(len(a))

#~ Check String
# To check if a certain phrase or character is present in a string, 
# we can use the keyword in.

# txt = "The best things in life are free!"
# print(txt)
# print("free" in txt)

#~ Check if NOT
# To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword not in.

txt = "The best things in life are free!"
# print("expensive" not in txt)
print(txt.upper())
print(txt.lower())
