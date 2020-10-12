numbers = [14, 15, 16, 17, 18]
number_bytes_list = [number.to_bytes(1, byteorder="big") for number in numbers]
print(number_bytes_list)
