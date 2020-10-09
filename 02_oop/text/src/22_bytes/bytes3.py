blist = bytes([1, 0])
print(blist)
print(int.from_bytes(blist, byteorder="big"))
