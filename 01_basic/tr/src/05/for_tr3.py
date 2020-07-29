start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

for i in range(start, stop, step):
    if stop <= i + step:
        print(i)
    else:
        print(i, end=", ")
