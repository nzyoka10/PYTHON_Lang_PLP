# PYTHON Tuple data type
# Tuples are ordered and immutable. 
# They can contain elements of any data type, including other tuples. 
'''
myTuple = ('ABCD', 56,  'Nairobi', 3+7j, 70.2)
# print(myTuple)
# slicing tuple
# print(myTuple[1:4])   # Output: ( 56, 'Nairobi', 3+7j)
                       # The slice starts from index  1 and ends at index 4 (not inclusive).
# print(myTuple * 3)
tinyTuple = 'Wed', 'Mon', 'Fri', 34.7
print(myTuple + tinyTuple)
'''

# tuple within a tuple
new = (
    [1, 2, 3], 
    'Kenya', 'Cool', 
    ('a', 'b', 'c', 'd', 'e', 'f')
)
print(new)
print(len(new))
print(new[2])







