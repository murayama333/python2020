x_list = [int(x) for x in input("X: ").split(" ")]
y_list = [int(y) for y in input("Y: ").split(" ")]
try:
    for i in range(len(x_list)):
        z = x_list[i] / y_list[i]
        print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
except IndexError as e:
    print("IndexError", e)
