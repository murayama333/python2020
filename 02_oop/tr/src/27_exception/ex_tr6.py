class DuplicateInput(Exception):
    pass


input_list = []
try:
    while True:
        value = input("Input: ")
        if value in input_list:
            raise DuplicateInput()
        input_list.append(value)
except DuplicateInput as e:
    print(input_list)
