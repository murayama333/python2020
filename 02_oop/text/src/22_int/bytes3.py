blist = [0x41, 0x70, 0x70, 0x6c, 0x65]
bytearray_data = bytearray(blist)

bytearray_data[0] = 0x61
str = bytearray_data.decode("UTF-8")
print(str)
