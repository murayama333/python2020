b_list = [0x48, 0x61, 0x6c, 0x6c, 0x6f]
b_array = bytearray(b_list)
b_array[1] = 0x65
str = b_array.decode("UTF-8")
print(str)
