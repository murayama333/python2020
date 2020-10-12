filename = input("File Name: ")
try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"{filename} is not found.")