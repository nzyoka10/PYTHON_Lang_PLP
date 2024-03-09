# 
# * Python
# Week 3 coding challenge
"""
    #* Checks if the result of base raised to the exponent is greater than 5000.

        #~ Args:
        #~ base (int): The base number.
        #~ exponent (int): The exponent.

    #* Returns:
    #& bool: True if the result is greater than 5000, False otherwise.

"""

# create function larger_power
def large_power(base, exponent):
    
    #~ Calculate the result of base raised to the exponent
    result = base ** exponent
    
    #~ Check if the result is greater than 5000
    if result > 5000:
        return True
    
    else:
        return False
    
# Print the result of calling the function with arguments 2 and  16
print(large_power(2,  16)) # Output: True
print(large_power(4, 21)) # Output: True

print('\n')

print(large_power(3, -7)) # Output: False
print(large_power(-7, 13)) # Output: False

print('\n')

print(large_power(3, 8)) # Output: True
print(large_power(-7, 12)) # Output: True



