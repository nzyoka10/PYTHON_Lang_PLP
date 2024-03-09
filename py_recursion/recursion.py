# 
# ** Recursion in Python
#^   Definition: A function calling itself
# 

def add_one(number):
    
    if (number >= 9):
        return number + 1
    
    total = number + 1
    print(total)
    
    return add_one(total)

my_new_total = add_one(0)
print(my_new_total)
print(type(my_new_total))






