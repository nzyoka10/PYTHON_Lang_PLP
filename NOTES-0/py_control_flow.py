# if statement
# it executes both True or False part of the code block.

# Example 1

# x = 1
# if x > 5:
#     print("x is greater than 5")
# print("Done")

# Example 2
# 
# temperature = -1
# if temperature < 0:
#     print("It's cold outside.")
    
# elif temperature >= 0 and temperature <= 30:
#         print("It's a nice day.")
        
# else:
#     print("It's hot outside.")
    
# print("\n\t End of program.")

''' 
    # Python Flow Controls :-> defines the flow of the execution of program....
    
    # if -- else
    # nested if -- else
    # for loop
    # while loop
    # break statement
    # continue statement
    
========== NOTES   =============
    
    #~   if -- else SYNTAX
# 
# ^        if ( condition ) :
# *               # code to be executed if the condition is true
# ^          else: 
# *               # code to be executed if the condition is false
# 
# !               .endif

====================================================

# ~ nested if -- else SYNTAX
#
# !       if ( condition1 ) :
# *             statement 1 to be executed if the condition is true.
# !        elif ( condition2 ) :
# *             statement 2 to be executed if the condition is false. 
#                            but when this condition becomes true then no further checking will happen, 
# !        else:
# *            statement 3 to be executed if the condition is false in both conditions above.
# 


===========================================

# ~    for statement SYNTAX
# 
# !      for iterating_var in sequence:
#  *          statements to be repeated for each element of the sequence.
# 





    
'''


    #~   if -- else SYNTAX
# 
# ^        if ( condition ) :
# *               # code to be executed if the condition is true
# ^          else: 
# *               # code to be executed if the condition is false
# 
# !               .endif

# Example 
# age = 12

# if age > 10 :
#     print("Hello, young soldier!")



# ~ nested if -- else SYNTAX
#
# !       if ( condition1 ) :
# *             statement 1 to be executed if the condition is true.
# !        elif ( condition2 ) :
# *             statement 2 to be executed if the condition is false. 
#                            but when this condition becomes true then no further checking will happen, 
# !        else:
# *            statement 3 to be executed if the condition is false in both conditions above.
# 

# !  Example 
# age = 40

# if age <= 10 :
#     print("\n Hello, young soldier!")
    
# elif age >= 11 and age <= 33:
#     print("\n You are a middle-aged person.")
    
# else:
#     print("\n Senior citizen")
    

# ~    for statement SYNTAX
# 
# !      for iterating_var in sequence:
#  *          statements to be repeated for each element of the sequence.
# 

# !   Example
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# for x in days:
#     print(x)

# ~   while loop SYNTAX
# 
# !      while ( condition is True ) :
# *           statements to be repeated until the condition is False. 
#  

# !   Example with While Loop 
# num = 5
# while num > 7:
#     print("Hello World")

#  example 2
# k = 1
# while k < 27:
#     print(k)
#     # k += 1
#     # k += 2 

# ! Example 3
# n = int(input('Enter an integer:'))
# while n != 0:
#     print(n)
#     n -= 1

# ! Example 3
# i = 9
# while i < 21:
#     if(i%3 == 0):
#         print(i, " : This is an ODD number!")
#     else:
#         print(i," : This is an Even number!")
#     i+=1

#* Break keyword - used to stop execution of enclosing loop or switch structure. It may also be used to skip some iteration(s

#~  break keyword - used to stop execution of loop prematurely.
# ~   Syntax
# !^      break [loop_name]
# *   Example with Break Keyword
# i = 0
# while i < 7:
#     if i == 5:
#         break         # This will terminate the loop when value of "i" becomes 3
#     print(i, end=" ")
#     i += 1            # Incrementing counter variable by 1 after every iteration.
#     # ! Output : 0, 1, 2, 3, 4
# print()              # Printing a new line  

# ? Example 2
# ? use --- Break statement
# j = 10
# while j > 0:
#     if (j!=5):
#         print(j)
#     # if (j % 2 == 0):
#     #     print(j, j % 2 == 0)
#     else:
#         break
#     j -= 1
# print("Outside Loop")





# * continue keyword - used to skip the rest of the code inside the loop and jump directly to next iteration.
# # !   Syntax
# # !       continue [loop_name]

# # !   Example with Continue Keyword
for j in range(5):
    if j == 3:
        continue      # Skipping the rest of the code inside this 'if' block and going to next iteration.
    print(j, end=' ')
print()               # Printing a new line  


# # Nested Loops or Control Flow - When one loop is inside another loop.

# # !   Example with Nested Loops
# outer_counter = 0
# while outer_counter < 3:                                          # Outer Loop runs 3 times
#     inner_counter = 0
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     while inner_counter < 4:                                     # Inner Loop runs 4 times for each time Outer Loop Runs
#     print("inner loop starting")
#     while inner_counter < 4:                                     # Inner Loop runs 4 times
#         print(f"Outer {outer_counter+1}:{inner_counter+1}")     # Displaying the values of counter and also showing which loop it belongs to. 

