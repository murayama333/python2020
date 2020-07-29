name_list = ["Alice", "Bob", "Charie", "Daniel"]
name_ex_list = [str(i + 1) + ":" + n for i, n in enumerate(name_list) if i % 2 == 0]
print(name_ex_list)
