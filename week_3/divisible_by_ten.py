# 
# ~  Divisible_by_ten.py
"""
    #~ Determines whether a number is divisible by ten.

        # * Args:
        # * num (int): The number to be checked.

    #!     Returns:
    #*          bool: True if num is divisible by ten, False otherwise.
    
"""

def divisible_by_ten(num):
    
    # Calculate the remainder of the number divided by 10
    remainder = num % 10
    
    # Check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Output of the function
print(divisible_by_ten(0))  # Output: True
print(divisible_by_ten(10))  # Output: True 
print(divisible_by_ten(20))  # Output: True 

print('\n')

print(divisible_by_ten(3))  # Output: False 
print(divisible_by_ten(9))  # Output: False
print(divisible_by_ten(-9))  # Output: False

print('\n')

print(divisible_by_ten(100))
print(divisible_by_ten(25))  # Output: False
print(divisible_by_ten(15))  # Output: False

