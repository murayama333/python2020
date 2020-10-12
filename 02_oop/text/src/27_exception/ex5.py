class MyError(Exception):
    pass


def check_value(value):
    if value < 0:
        raise MyError(f"Invalid value: {value}")
    return "OK"


try:
    print(check_value(1))
    print(check_value(-1))

except MyError as e:
    print(e)
