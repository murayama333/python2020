def same_value_list(size=9, value=1):
    return [value for _ in range(size)]

def random_value_list(size=9, start=1, end=9):
    from random import randint
    return [randint(start, end) for _ in range(size)]
