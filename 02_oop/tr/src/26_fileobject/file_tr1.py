my_list = list(range(1, 10))
file = "my_list.txt"
with open(file, "w") as f:
    for value in my_list:
        f.write(f"{value}\n")