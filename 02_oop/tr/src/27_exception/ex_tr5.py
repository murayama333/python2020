class LoginError(Exception):
    pass


def login(id, password):
    if id == "alice" and password == "secret":
        return "LOGIN OK"
    else:
        raise LoginError("LOGIN ERROR")


try:
    id = input("ID: ")
    password = input("PASSWORD: ")
    if login(id, password):
        print("LOGIN OK")
except LoginError as e:
    print("LOGIN ERROR")
