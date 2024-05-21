
# Python operators
# ~ Arithmetic operators
# 

# a = 10
# b = 3

# print(a + b)  # Output: 13
# print(a - b)  # Output: 7
# print(a * b)  # Output: 30
# print(a / b)  # Output: 3.3333333333333335
# print(a % b)  # Output: 1
# print(a // b) # Output: 3
# print(a ** b) # Output: 1000

# program to print 1 to 10 in decimal and binary
# ~ decimal

# num = 1
# while num <= 10:
#     print(num)
#     num += 1
    
# print('\n')

# decimal_num = 21
# # bin_num_1 = (decimal_num /  2)
# bin_num = int(decimal_num)

# if decimal_num // 2 == 1 and bin_num % 2 == 1:
#     print("Decimal number", decimal_num)
# else:
#     print("Binary number", bin_num)
#     print(format(bin_num, '04b'))
#     print(format(bin_num, '08b'))
#     print(type(bin_num))

# print('\n')

decimal_num = 1
max_sum = (decimal_num // 2 and decimal_num % 2 == 1)

while max_sum < 5:
    print(max_sum)
    print(format(max_sum, '04b'))
    max_sum += 1










