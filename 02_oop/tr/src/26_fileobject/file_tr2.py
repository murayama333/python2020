file = "my_list.txt"
with open(file, "r") as f:
    lines = f.readlines()
print(sum([int(line.strip()) for line in lines]))
