# 
# ~ Python Bitwise Operators
# 
''' 
    # & Bitwise AND
    # | Bitwise OR
    # ^ Bitwise XOR
    # ~ Bitwise NOT
    # << Left shift
    # >> Right shift

'''


print('\n _______ Bitwise Operators ______')

a = 14  #*   0000 1110
b = 17  #*  0001 1111

print ('a =', a)
print('b =', b)

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a
left_shift = a << 2
right_shift = a >> 2

print("Bitwise AND: ", bitwise_and, " (%d)" % bitwise_and)
print("Bitwise OR: ", bitwise_or, " (%d)" % bitwise_or)
print("Bitwise XOR: ", bitwise_xor, " (%d)" % bitwise_xor)
print("Bitwise NOT (a): ", bitwise_not, " (%d)" % bitwise_not)
print("Left Shift: ", left_shift, " (%d)" % left_shift)
print("Right Shift: ", right_shift, " (%d)\n" % right_shift)

    
# print('c =', a & b  )


# * Example 3
# print('Bitwise AND: ', a & b)
# print('Bitwise OR :', a | b)
# print('Bitwise XOR:', a ^ b)
# print('Bitwise NOT:',  ~b)

# &  Example 2.
# print('\b a bitwise & (and) is : ', a & b)   # 14 & 17 => 14
# print(' \b b bitwise | (or) is : ', b | a)     # 17 | 14 => 17
# print(' \b ~a gives the one complement of a: ', ~a)      # ~14 => -15
# print(' \b a left shifted by 2 bits is : ', a<<2 )       # 14 << 2 =>  56
# print(' \b a right shifted by  2 bits is : ', a>>2 )     # 14 >> 2 =>  6

# print('\n')

#  Example 1
# a = 60  # 0011 1100
# b = 13  # 0000 1101

# print(a & b)  # Output: 12 (0000 1100)
# print(a | b)  # Output: 61 (0011 1101)
# print(a ^ b)  # Output: 49 (0011 0001)
# print(~a)     # Output: -61 (1100 0011)
# print(a << 2) # Output: 240 (1111 0000)
# print(a >> 2) # Output: 15 (0000 1111)

