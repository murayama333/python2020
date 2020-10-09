i = 15
b = i.to_bytes(1, byteorder="big")
print(b)

bit_length = i.bit_length()
print(bit_length)
