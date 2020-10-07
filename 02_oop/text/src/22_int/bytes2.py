blist = [0x41, 0x70, 0x70, 0x6c, 0x65]
bytes_data = bytes(blist)
# bytes_data = b"\x41\x70\x70\x6c\x65"
str = bytes_data.decode("UTF-8")
print(str)
