# 
# ~ Python functions
# 
# ~ Example 1
# def hello():
#     print("Hello World!")

# hello()

# ! Example 3:
# # * function to ADD to numbers
# def sum(num1, num2):
#     print("Sum: ", num1 + num2)
    
# sum(1, 4)
# sum(12, 4)
# sum(12, -44)

# Using the return keyword
def sum(num1, num2):
    
    # check if num1 and num2 are of type <int>
    if (type(num1) is not int or type(num2) is not int):
        return
    
    # return sum of num1 and num2 if : type == int
    return num1 + num2

# total = sum(2, 4)
# total = sum(12, 14)
total = sum('32', 45)

print("Total: ", total)








