class MyNotFoundError(Exception):
    pass


def search(lst, target):
    if target not in lst:
        raise MyNotFoundError(f"{target} is not found.")
    return f"{target} is found."


fruits = ["Lemon", "Orange", "Grape", "Banana", "Peach"]
targets = ["Orange", "Apple", "Lemon"]

for target in targets:
    try:
        print(search(fruits, target))
    except MyNotFoundError as e:
        print(e)
