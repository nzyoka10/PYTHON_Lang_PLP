# 
# ** Recursion in Python
#^   Definition: A function calling itself
# 

#     while (number >= 9):
#         return number + 1
#     # number = total
#     total = number + 1
#     return add_one(total)


def add_one(num):
    # * using while loop
    
    while(num <= 9):
        print(num) 
        num += 1
    
    total = num
    # print(total)
    return total
    
# add_one(0)
my_new_total = add_one(0)
print(my_new_total)
print(type(my_new_total))

        
    # total = number + 1
    # print(total)
    
         # Using while loop to print same output
    # count = 0
    # while number >= count:
        
#     return add_one(total)

# num = add_one(0)
# print(num)
        
    
    # if (number >= 9):
    #     return number + 1
    
    # total = number + 1
    # print(total)
    
#     return add_one(total)

# num = add_one(0)
# print(num)

# my_new_total = add_one(0)
# print(my_new_total)
# print(type(my_new_total))


   #     return number + 1
    # count += 1
        
        # if number >= count:
            # return number + 1
        
        # total = number + 1
        # print(total)
        
        
        





