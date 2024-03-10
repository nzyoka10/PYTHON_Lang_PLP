# 
# Python Identity Operators
# 

#~ Example
print('\n ____ Python Identity Operators _____')

x = ["apple", "banana"]
y = ["apple", "banana", "Orange"]
z = x

print(type(x))
print('\n elements of x : ', x)
print('\n elements of y : ', y)
print('\n elements of z : ', z)

print("\n Check identities:::------------------------")
print('x is z', x is z)  # Output: True
print('x is y', x is y)  # Output: True
print('x == y', x == y)  # Output: True

# print(x is y)  # Output: False, despite having the same content they are not the same object
# print(x == y)  # Output: True, since their content is the same
