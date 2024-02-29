# write a program that accepts  user input to create a list of integers.
# Then, compute the sum of all the integers in the list
''' 
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
print("Original List: ", my_list)
total = sum(my_list)
print("Sum of Integers in the List: ", total)
''' 

# take user input and create a list of integers from it
user_input = input("Enter numbers separated by comma: ")
nums = [int(x) for x in user_input.split(',')]
print("User Input as List: ", nums)
sum_list = sum(nums)
print('Sum of User Input: ', sum_list)