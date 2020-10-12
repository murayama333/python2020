numbers = [1, 2, 4, 8, 16]
number_bytes_list = [number.to_bytes(1, byteorder="big") for number in numbers]
print(number_bytes_list)
