b_list = [0x50, 0x79, 0x68, 0x74, 0x6f, 0x6e]
message_byte_array = bytearray(b_list)
message_byte_array[2], message_byte_array[3] = message_byte_array[3], message_byte_array[2]
print(message_byte_array.decode("UTF-8"))
