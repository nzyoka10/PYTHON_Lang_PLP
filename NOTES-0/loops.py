# 
# ! ---_____  == ___  Python Loops ___ == ___----
#  for --- loop 
#  while --- loop
# 
# * For example:
# names = ["Kenya", "United States", "China", "Tanzania", "Somalia"]

# for name in names:
#     print('\n', name)

# * For Loops : using Range
#   - The range() function returns a sequence of numbers. 
#   - It can take one, two or three arguments to define the range of values to generate. 

#  example
# welcome_msg = "Welcome to PLP"

# for i in range(5):                    # Loop will run 5 times
#     print('\n', welcome_msg)
    
# ** While Loops
#   - A while loop is used when we don't know how many times the loop needs to be repeated. 
''' 
    #!  Syntax
    # 
    # *   while condition:
    # *         code block to execute
    # 
'''
# Example:
# count = 0

# while count < 10:                        # This loop will continue until count becomes equal to 10
#     print("\n Count Value: ", count)       # Printing the value of count
#     count += 1                          # Increasing the value of count by 1 after each iteration
# print("\n\nLoop Ended")                # This message will be printed once the loop ends

# ! --___ Loop controls :: Break and Continue
# * Break : The break statement is used to exit from the loop prematurely. 
#           When the loop encounters a break statement, it immediately terminates and transfers control outside the loop.

# ~ Continue : The continue statement is used to skip the rest of the code inside the loop for a particular iteration and jump directly to the next iteration
# ~ Continue : The continue statement is used to skip the rest of the code inside the loop for this single iteration only.

# ^ Example 1 : Using for Loop:
# colors = ["Blue", "Red", "Green", "White", "Yellow", "Black"]
# color_i_want = "White"

# for color in colors:
#     if color == color_i_want:           
#         print("\n\n The color i want is:->  ", color_i_want)
#         break
    
#     print("\n Other colors:  ", color)
# print("Color Loop Ended")

# &  Example 2 : Using While Loop
colors = ["Blue", "Red", "Green", "White", "Yellow", "Black"]
color_i_want = "Green"

length = len(colors)
count = 0

while count < length:
    if colors[count] == color_i_want:           
        print("\n\n The color i want is:->  ", color_i_want)
        break
    count += 1
    
    print("\n Other colors:  ", colors)
# print("Color Loop Ended")



