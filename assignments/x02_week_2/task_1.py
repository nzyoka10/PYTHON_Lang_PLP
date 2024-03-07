
# program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.



# my_list = [1,2,3,4,5]
# sum = sum(my_list)
# print(len(my_list))
# print(sum)
# print(sum(my_list))

my_list = input("Enter your list of integers, separated by comma: ")

nums = [
    int(x) for x in my_list.split(',')
]
print("My list contains: ", nums)

sum_of_list = sum(nums)
print("Sum of list: ", sum_of_list)

