
# 
#** Exercise - Write a program that converts binary to decimal and vice versa.
# 

# def convertBinaryToDecimal(binary):
    
#     ''' Convert Binary number to Decimal number '''
#     return int(binary, 2)

    
def convert_decimal_to_binary(decimal):
    
    ''' Convert Decimal number to Binary number '''
    return decimal_number.replace("0b", "")

# binaryNumber = input("\n Enter the binary number you want to convert to Decimal:\t")
decimal_number = input("\n Enter the decimal number you want to convert to Binary:\t")

if decimal_number.isdigit():
    print ("\nYour binary number is : ", convert_decimal_to_binary(decimal_number))
# else:
#     print ("\nYour decimal number is : ", convertDecimalToBinary(int(decimalNumber)))