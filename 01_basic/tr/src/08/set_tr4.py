names = set()
while True:
    name = input("Name: ")
    if name == "":
        break
    names.add(name)
    
print("Names:", names)