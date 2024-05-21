#~ 
# ^   Conditional statements: (If, if...else, if...elif...else)
# *
#~ Conditional statements helps in decision-making process, 
# ~
# !        For example,
#*  “Are you hungry? If so, then eat” is a conditional statement
#* Phrased as: - If you’re hungry, then eat
''' 
    # Let's break this down to pick a boolean expression in our conditional statement.

    # “Are you hungry” is the boolean expression here, so the conditional statement is checking if it’s True.
    # If “are you hungry” == True, the conditional statement will be executed and you will eat.
    # If [you are hungry], then [eat food]

        # if hungry:
        #     print("Eat Food!")
    
'''
# ! Python has 2 types of conditional flows
# *     1. conditional statement (if, else or elif )
# *     2. Loops (for loop and while loop)


#  if statement
    # num = 20
    # if num > 15:
    #     print("NUM is: ", num)
    
# * if --- else statement
    # num = 18
    # if num > 105:
    #     print("Number is: ", num)
    # else:
    #     print("Sorry NUM is not greater than 15, num is:-> ", num)

# * if...elif...else statement
# num = 317
# print("Conditional Statement with 'if...elif...else': \n")

# if num < 15:
#     print("Number is:.--> ", num)
    
# elif num >= 16 and num <= 30:   # range from 16 to 30 inclusive
#     print("Youngster!!!, Number is: -->", num)
    
# else:                           # anything above 30
#     print("Oldster!!! , Number is: -->", num)

# ! Example 2
weekday = False
weekday = True

if weekday:
    print("wake up at 6:30")
else:
    print("Sleep in")








