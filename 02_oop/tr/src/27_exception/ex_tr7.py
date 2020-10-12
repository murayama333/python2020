class MyRequiredError(Exception):
    pass


class MyLengthError(Exception):
    pass


def validate(value, length):
    if len(value) == 0:
        raise MyRequiredError()
    if len(value) > length:
        raise MyLengthError()


try:
    value = input("Input: ")
    validate(value, 5)
    print(value)
except MyRequiredError as e:
    print("MyRequiredError")
except MyLengthError as e:
    print("MyLengthError")
