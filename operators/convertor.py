
# 
#** Exercise - Write a program that converts decimal to binary and vice versa. 
# 

# decimal_num = 7
# binary_num_1 = decimal_num // 2
# binary_num = binary_num_1 % 2

# print("decimal_number: ", decimal_num)
# # print("binary_number: ", bin(binary_num), end="\n")
# print("binary_number: ", format(binary_num, '04b'), end="\n")

# print(bin(7), end="\n")


print(format(7,'04b'))  # This specifies leading 0, 8 digits, binary.
# 10100000





































# def convertBinaryToDecimal(binary):
    
#     ''' Convert Binary number to Decimal number '''
#     return int(binary, 2)

    
# def convert_decimal_to_binary(decimal):
    
#     ''' Convert Decimal number to Binary number '''
#     return decimal_number.replace("0b", "")

# # binaryNumber = input("\n Enter the binary number you want to convert to Decimal:\t")
# decimal_number = input("\n Enter the decimal number you want to convert to Binary:\t")

# if decimal_number.isdigit():
#     print ("\nYour binary number is : ", convert_decimal_to_binary(decimal_number))
# else:
#     print ("\nYour decimal number is : ", convertDecimalToBinary(int(decimalNumber)))