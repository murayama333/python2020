str = "Hello World"

l_find = str.find("l")
print("l find:", l_find)
x_find = str.find("x")
print("x find:", x_find)

try:
    l_index = str.index("l")
    print("l index:", l_index)
    x_index = str.index("x")
    print("i index:", x_index)
except ValueError as e:
    print(e)

l_in_str = "l" in str
print("l in str:", l_in_str)
x_in_str = "x" in str
print("x in str:", x_in_str)
