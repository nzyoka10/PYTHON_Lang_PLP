'''
    # Why Use Lambda Functions?
        # The power of lambda is better shown when you use them as an anonymous function inside another function.

    # Example: you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

'''
# Example 1
# def my_function(n):
#     return lambda a : a * n

# print(my_function(5)(7))

# Example 2
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

#~ Example 3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(12)
mytripler = myfunc(7)

print(mydoubler(11))
print(mytripler(11))


