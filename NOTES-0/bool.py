# Use BOOLEAN logic in PYTHON
# their value can only ever be one of two things: True or False
# Scenario: Print warning messages

# Write 'if' statements
# To express conditional logic in Python, you use if statements
''' 
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b



# test this expression
k = 24
n = 44
if k <= 0:
    print(k)
print(n)

# Work with else statement
# The 'else' clause is used with the 'if' statement. It executes when the condition is not met.

#   SYNTAX 

# if test_expression:
    #   statement(s) to be run
# else:
    #   statement(s) to be run

# Example
a = 98
b = 55
if a < b:
    print("Warning!", a, "is less than", b)
else:
    print(a, "is not less than", b)
    print()
    
    
# Combine if, elif, and else statements
    ''' 
    ''' 
    if test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
elif test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
else:
    # statement(s) to be run
    
''' 


a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")
    


a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")