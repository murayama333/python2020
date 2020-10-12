f = open("names.txt", mode="r")
lines = f.readlines()
f.close()
for line in lines:
    print(line)
