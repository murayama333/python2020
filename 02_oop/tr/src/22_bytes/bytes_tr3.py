numbers = [256, 512, 1024, 2048 , 4096]
for number in numbers:
    print(number.to_bytes(2, byteorder="big"))
